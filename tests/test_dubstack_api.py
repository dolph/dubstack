import json

from dubstack import client
from dubstack import test
from dubstack import utils


class DubstackApi(test.TestCase):
  def setUp(self):
    super(DubstackApi, self).setUp()
    self.options = self.appconfig('default')
    app = self.loadapp('default')
    self.app = app

    self.dubstep_backend = utils.import_object(
        self.options['bass_driver'], options=self.options)
    self._load_fixtures()

  def _load_fixtures(self):
    pass

  def _login(self):
    c = client.TestClient(self.app)
    post_data = {'user_id': self.user_foo['id'],
                 'tenant_id': self.tenant_bar['id'],
                 'password': self.user_foo['password']}
    resp = c.post('/tokens', body=post_data)
    token = json.loads(resp.body)
    return token

  def test_generate_lyrics(self):
    expected_lyrics = \
        "aroow aroow aroow aroow\n" \
        "aroow aroow aroow aroow\n" \
        "bum bum bum\n" \
        "bum bum bum"
    c = client.TestClient(self.app)
    post_data = {'input': 'ab'}
    resp = c.generate(**post_data)
    data = json.loads(resp.body)
    self.assertEquals(expected_lyrics, data['lyrics'])
