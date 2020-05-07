import os
import json
import requests

class Facebook:
    @staticmethod
    def get_access_token(token_name):
        access_token = os.getenv('PWD') + '/access_tokens.sh'
        f = open(access_token, 'r+')
        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split('=')
            if tokens[0] == token_name:
                return tokens[1].strip()

        return 'Not found'

    def __init__(self):
        self.page_id = Facebook.get_access_token('FACEBOOK_PAGE_ID')
        self.page_access_token = Facebook.get_access_token('FACEBOOK_PAGE_ACCESS_TOKEN')



    def publish_photo_msg(self, message, image_url):
        data={
            'url':image_url,
            'published': 'true',
            'access_token': self.page_access_token,
            'caption':message
            }
        response=requests.post('https://graph.facebook.com/'+self.page_id+'/photos',data=data)
        print(response.status_code,response.json())
        return

if __name__ == '__main__':
    facebook = Facebook()
    # TODO: CRIO_TASK_MODULE_FACEBOOK_SHARE_FROM_CLI
    # Tasks:
    # 1) Search for your favorite ice-cream picture on images.google.com
    # 2) Copy the URL of the image and assign it to the 'image_url' variable
    #    Eg: image_url = 'http://ksmartstatic.sify.com/cmf-1.0.0/appflow/bawarchi.com/Image/oeturjecjjdah_bigger.jpg'
    # 3) Fill the 'my_name' variable with your name so that you know the posts you have created
    image_url = 'https://assetsds.cdnedge.bluemix.net/sites/default/files/styles/very_big_1/public/feature/images/ice_cream_1.jpg'
    my_name = '@desh_1997'

    message = my_name + ' likes this ice-cream!'
    facebook.publish_photo_msg(message, image_url)
