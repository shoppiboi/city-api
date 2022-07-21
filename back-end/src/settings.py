import os
import configparser


def load_config():
  """
  Loads variables from ../environments/local.ini and
  ../environments/local.secrets.ini and exports them as
  environment variables to run app locally
  """
  config_file_paths = [
      "../../environments/local.ini",
      "../../environments/local.secrets.ini",
  ]

  for config_file_path in config_file_paths:
      config = configparser.ConfigParser()
      config.read(config_file_path)

      for section in config.sections():
          for key in config[section]:
              os.environ[f"{section}_{key}".upper()] = config[section][key]
