from dubstack import utils


class Manager(object):
  def __init__(self, options):
    self.driver = utils.import_object(options['bass_driver'],
        options=options)
    self.options = options

  def generate(self, context, source):
    # this should become tenant id when middleware is implemented
    tenant = context['token_id']
    return self.driver.generate(tenant, source)

  def play(self, context):
    # this should become tenant id when middleware is implemented
    tenant = context['token_id']
    return self.driver.play(tenant)
