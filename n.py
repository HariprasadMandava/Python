from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

baseurl = 'https://your_company.sharepoint.com'
basesite = '/path/to/site' # every share point has a home.
siteurl = baseurl + basesite

localpath = 'Documents/file.txt'
remotepath = Shared Documents/file.txt # existing folder path under sharepoint site.

ctx_auth = AuthenticationContext(url)
ctx_auth.acquire_token_for_user(username, password)
ctx = ClientContext(siteurl, ctx_auth) # make sure you auth to the siteurl.

with open(localpath, 'rb') as content_file:
    file_content = content_file.read()

dir, name = os.path.split(remotepath)
file = ctx.web.get_folder_by_server_relative_url(dir).upload_file(name, file_content).execute_query()