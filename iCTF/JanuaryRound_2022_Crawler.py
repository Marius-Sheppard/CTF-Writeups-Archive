import requests;
from bs4 import BeautifulSoup;

Sessy = requests.Session();
BaseURL = "http://137.184.207.224:1111/";

def Grab(URL):
    ToFollow = [];
    Response = Sessy.get(URL);
    Page = Response.content;
    Good_Soup = BeautifulSoup(Page, "lxml");

    for Link in Good_Soup.findAll('a'):
        ToFollow.append(Link.get('href'));
    
    if(ToFollow != []):
        print(ToFollow);

    return ToFollow;



def Spam(ToFollow):

    for Link in ToFollow:
        Response = Sessy.get(BaseURL + Link);
        Page = Response.content;
        # print(Page);
        if Page.find(b"ictf") != -1 or Page.find(b"flag") != -1:
            print(Page);


        Spam(Grab(BaseURL + Link));
 

Spam(Grab(BaseURL));