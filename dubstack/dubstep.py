from dubstack import utils


class Manager(object):
  def __init__(self, options):
    self.driver = utils.import_object(options['bass_driver'],
        options=options)
    self.options = options

  def generate(self, context, source):
    return self.driver.generate(source)
