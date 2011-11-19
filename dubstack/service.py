import json
import logging

import routes
import webob.dec
import webob.exc

from dubstack import dubstep
from dubstack import wsgi


URLMAP = {
    'generate': ('POST', '/wompwomps'),
    'play': ('GET', '/wompwomps')}


class BaseApplication(wsgi.Application):
  @webob.dec.wsgify
  def __call__(self, req):
    arg_dict = req.environ['wsgiorg.routing_args'][1]
    action = arg_dict['action']
    del arg_dict['action']
    del arg_dict['controller']
    logging.debug('arg_dict: %s', arg_dict)

    context = req.environ.get('openstack.context', {})
    # allow middleware up the stack to override the params
    params = {}
    if 'openstack.params' in req.environ:
      params = req.environ['openstack.params']
    params.update(arg_dict)

    # TODO(termie): do some basic normalization on methods
    method = getattr(self, action)

    # NOTE(vish): make sure we have no unicode keys for py2.6.
    params = dict([(str(k), v) for (k, v) in params.iteritems()])
    result = method(context, **params)

    if result is None or type(result) is str or type(result) is unicode:
      return result

    return json.dumps(result)


class DubstepController(BaseApplication):
  """Validate and pass calls through to DubstepManager.

  DubstepManager will also pretty much just pass calls through to
  a specific bass driver.
  """

  def __init__(self, options):
    self.dubstep_api = dubstep.Manager(options=options)
    self.options = options

  def noop(self, context, *args, **kw):
    return ''

  def generate(self, context, **kwargs):
    text = kwargs.get('input')
    logging.debug('SOURCE TEXT: %s', text)
    lyrics = self.dubstep_api.generate(context, text)
    logging.debug('LYRICS: %s', lyrics)
    return {'lyrics': lyrics}


class Router(wsgi.Router):
  def __init__(self, options):
    self.options = options
    self.dubstep_controller = DubstepController(options)

    mapper = self._build_map(URLMAP)
    mapper.connect('/', controller=self.dubstep_controller, action='noop')
    super(Router, self).__init__(mapper)

  def _build_map(self, urlmap):
    """Build a routes.Mapper based on URLMAP."""
    mapper = routes.Mapper()
    for k, v in urlmap.iteritems():
      controller = self.dubstep_controller
      action = k
      method, path = v
      path = path.replace('%(', '{').replace(')s', '}')

      mapper.connect(path,
        controller=controller,
        action=action,
        conditions=dict(method=[method]))

    return mapper


def app_factory(global_conf, **local_conf):
  conf = global_conf.copy()
  conf.update(local_conf)
  return Router(conf)
