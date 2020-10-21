# Get string before a token
def get_pre_token(str , token):
  return str[:str.index(token)]

# Get string after a token
def get_after_token(str , token):
  return str[str.index(token)+1:]