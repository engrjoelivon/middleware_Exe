from django import http

from django.utils.datastructures import MultiValueDictKeyError


class ChangeRequest:
    def process_request(self,request):
        #print("handle request method ",request.path)
        #request.path="/ABC/"
        #print("handle request method ", request.path)
        pass


    def process_view(self,request,view_func,view_args,view_kwargs):
        return None


    def process_template_response(self,request, response):
        """
        if response.is_rendered:
            #print("yes it has been rendered")
        else:
            print("No it has not been renderd")

        """

        print("def process_template_response ",response.context_data)
        new_dic = {"age": 25}
        z = response.context_data.copy()
        z.update(new_dic)



        response.context_data=z
        print("def process_template_response ",response.context_data)

        return response
    def process_exception(self,request,exception):
        print("there was a big exceptiojns",exception)