from requests import get
import time

def usernameSearch():
    username = input("Enter Username: ").lower()
    
    #twitter user search
    twitterurl = 'https://twitter.com/' + username
    twitterresponse = get(twitterurl, headers=headers)
    if twitterresponse.status_code == 200:
        print('Twitter [-]')
    else:
        print('Twitter [+]')

    #tumblr user search
    tumblrurl = 'https://' + username + '.' + 'tumblr.com'
    tumblrresponse = get(tumblrurl, headers=headers)
    if tumblrresponse.status_code == 200:
        print('Tumblr [-]')
    else:
        print('Tumblr [+]')

    #viber user search
    viberurl = 'https://chats.viber.com/' + username
    viberresponse = get(viberurl, headers=headers)
    if viberresponse.status_code == 200:
        print('Viber [-]')
    else:
        print('Viber [+]')

    #vk user search
    vkurl = 'https://vk.com/' + username
    vkresponse = get(vkurl, headers=headers)
    if vkresponse.status_code == 200:
        print('VK [-]')
    else:
        print('VK [+]')

    #pinterest user search
    pinteresturl = 'https://pinterest.com/' + username
    pinterestresponse = get(pinteresturl, headers=headers)
    if pinterestresponse.status_code == 200:
        print('Pinterest [-]')
    else:
        print('Pinterest [+]')

    #reddit user search
    redditurl = 'https://reddit.com/user/' + username
    redditresponse = get(redditurl, headers=headers)
    if redditresponse.status_code == 200:
        print('Reddit [-]')
    else:
        print('Reddit [+]')

    #taringa user search
    taringaurl = 'https://taringa.net/' + username
    taringaresponse = get(taringaurl, headers=headers)
    if taringaresponse.status_code == 200:
        print('Taringa [-]')
    else:
        print('Taringa [+]')

    #tagged user search
    taggedurl = 'http://tagged.com/' + username
    taggedresponse = get(taggedurl, headers=headers)
    if taggedresponse.status_code == 200:
        print('Tagged [-]')
    else:
        print('Tagged [+]')

    #badoo user search
    badoourl = 'https://badoo.com/profile/' + username
    badooresponse = get(badoourl, headers=headers)
    if badooresponse.status_code == 200:
        print('Badoo [-]')
    else:
        print('Badoo [+]')

    #github user search
    githuburl = 'https://github.com/' + username
    githubresponse = get(githuburl, headers=headers)
    if githubresponse.status_code == 200:
        print('Github [-]')
    else:
        print('Github [+]')
    
    #myspace user search
    myspaceurl = 'https://myspace.com/' + username
    myspaceresponse = get(myspaceurl, headers=headers)
    if myspaceresponse.status_code == 200:
        print('Myspace [-]')
    else:
        print('Myspace [+]')

    #mix user search (originally stumbledupon
    mixurl = 'https://mix.com/' + username
    mixresponse = get(mixurl, headers=headers)
    if mixresponse.status_code == 200:
        print('Mix [-]')
    else:
        print('Mix [+]')

    #wattpad user search
    wattpadurl = 'https://wattpad.com/user/' + username
    wattpadresponse = get(wattpadurl, headers=headers)
    if wattpadresponse.status_code == 200:
        print("Wattpad [-]")
    else:
        print("Wattpad [+]")

    #deviantart user search
    deviantarturl = 'https://deviantart.com/' + username
    deviantartresponse = get(deviantarturl, headers=headers)
    if deviantartresponse.status_code == 200:
        print('Deviant Art [-]')
    else:
        print('Deviant Art [+]')

    #goodreads user search
    goodreadsurl = 'https://goodreads.com/' + username
    goodreadsresponse = get(goodreadsurl, headers=headers)
    if goodreadsresponse.status_code == 200:
        print('Good Reads [-]')
    else:
        print('Good Reads [+]')
    
    #couchsurfing user search
    couchsurfurl = 'https://couchsurfing.com/people/' + username
    couchsurfresponse = get(couchsurfurl, headers=headers)
    if couchsurfresponse.status_code == 200:
        print('Couch Surfing [-]')
    else:
        print('Couch Surfing [+]')
    
    #ask.fm user search
    askfmurl = 'https://ask.fm/' + username
    askfmresponse = get(askfmurl, headers=headers)
    if askfmresponse.status_code == 200:
        print('Ask Fm [-]')
    else:
        print('Ask Fm [+]')

    #flickr user search
    flickrurl = 'https://flickr.com/' + username
    flickrresponse = get(flickrurl, headers=headers)
    if flickrresponse.status_code == 200:
        print('Flickr [-]')
    else:
        print('Flickr [+]')

    #imgur user search
    imgururl = 'https://imgur.com/user/' + username
    imgurresponse = get(imgururl, headers=headers)
    if imgurresponse.status_code == 200:
        print('Imgur [-]')
    else:
        print('Imgur [+]')

    #soundcloud user search
    scurl = 'https://soundcloud.com/' + username
    scresponse = get(scurl, headers=headers)
    if scresponse.status_code == 200:
        print('Soundcloud [-]')
    else:
        print('Soundcloud [+]')

    #minds user search
    mindsurl = 'https://minds.com/' + username
    mindsresponse = get(mindsurl, headers=headers)
    if mindsresponse.status_code == 200:
        print('Minds [-]')
    else:
        print('Minds [+]')

    #delicious user search
    deliciousurl = 'https://del.icio.us/' + username
    deliciousresponse = get(deliciousurl, headers=headers)
    if deliciousresponse.status_code == 200:
        print('Delicious [-]')
    else:
        print('Delicious [+]')
