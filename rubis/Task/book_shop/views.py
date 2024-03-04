from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import review, book
from rest_framework.response import Response
from rest_framework.views import APIView
from.serializer import review_serializer, book_serializer
import smtplib
from .validation import Book_validate, Review_validate
import json



class Book(APIView):
    permission_classes = [IsAuthenticated]
    """
    This function reterive, post, update, delete all book data's, if pass the filter it will return the filtered data 
    based on the specific requirment.

    params:
        {
        "filter":"None"
        }
    
        {
        "filter":"id",
        "ids":[1,2,3]
        }
    
    """
    def get(self, request):
        try:
            data = request.data
            filter = data.get('filter')
            if filter == 'id':
                query = book.objects.filter(id__in=data.get('ids'))
            elif filter == 'author':
                query = book.objects.filter(id__in=data.get('authors'))
            elif filter == 'publication_year':
                query = book.objects.filter(id__in=data.get('publication_years'))
            else:
                query =book.objects.all()
            serializer = book_serializer(query, many=True)
            return Response({"status":"sucess","data":serializer.data}, status=200)
        except Exception as e:
            return Response({"status":"failure", "message":str(e)}, status=500)
    """
    params:
        {
        "title":"wings of fire",
        "author": "kalam",
        "publication":"sumathi publication",
        "year": "25-01-1999"
        }
    """
    def post(self, request):
        try:
            data = request.data
            # Attempt validation using pydantic
            try:
                Book_validate.parse_raw(json.dumps(data))
            except Exception as e:
                print(str(e))
                return Response({"status":"failure", "message":"validation failed"}, status=402)
            serializer = book_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors())
                return Response({"status":"failure"}, status=402)
            return Response({"status":"sucess"}, status=200)
        except Exception as e:
            return Response({"status":"failure", "message":str(e)}, status=500)
        
    
    """
    params:
        {
        "id":"1"
        }

    """
    def delete(self, request):
        try:
            data = request.data
            id = data.get('id')
            query = book.objects.get(pk=id)
            query.delete()
            return Response({"status":"sucess"}, status=200)
        except Exception as e:
            return Response({"status":"failure", "message":str(e)}, status=500)
        
    """
    params:
        {
        "id":"1",
        "title":"wings of fire",
        "author": "kalam",
        "publication":"sumathi publication",
        "year": "25-01-1999"
        }

    """
    def update(self, request):
        try:
            data = request.data
            id = data.get('id')
            book.objects.filter(id=id).update(title=data.get('title'), author=data.get('author'),
                                                      publication=data.get('publication'), year=data.get('year'))
            return Response({"status":"sucess"}, status=200)
        except Exception as e:
            return Response({"status":"failure", "message":str(e)}, status=500)
    

    

class Review(APIView):
    permission_classes = [IsAuthenticated]
    """
    This function reterive, post, update, delete the review of the book we want.follow the 
    given parameters 

    params: 
        {
        "book_id": 1
            }
    """
    def get(self, request):
        try:
            data = request.data
            book_id = data.get('book_id')
            query = review.objects.filter(book=book_id)
            serializer = review_serializer(query, many=True)
            return Response({"status":"sucess","data":serializer.data}, status=200)
        except Exception as e:
            return Response({"status":"failure", "message":str(e)}, status=500)
        
    def send_mail(self,):
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("email_id", "password")
            message = "Sucessfully added the review, Thankoy for your response"
            s.sendmail("sender_email_id", "receiver_email_id", message)
            s.quit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def post(self, request):
        """
        params: 
        {
        "book_review":"Good book",
        "rating": 5,
        "book": 1
            }
        """
        try:
            data = request.data
            # Attempt validation using pydantic
            try:
                Review_validate.parse_raw(json.dumps(data))
            except Exception as e:
                print(str(e))
                return Response({"status":"failure", "message":"validation failed"}, status=402)
            
            serializer = review_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors())
                return Response({"status":"failure"}, status=402)
            if not self.send_mail(): # To send email dummy email is given
                return Response({"status":"failure"}, status=402)
            return Response({"status":"sucess"}, status=200)
        except Exception as e:
            return Response({"status":"failure", "message":str(e)}, status=500)
        
    """
    params:
        {
        "id":"1"
        }

    """
    def delete(self, request):
        try:
            data = request.data
            id = data.get('id')
            query = review.objects.get(pk=id)
            query.delete()
            return Response({"status":"sucess"}, status=200)
        except Exception as e:
            return Response({"status":"failure", "message":str(e)}, status=500)
    

    """
    params:
        {
        "id":"1",
        "book_review":"update",
        "rating": "2",
        }

    """
    def update(self, request):
        try:
            data = request.data
            id = data.get('id')
            review.objects.filter(id=id).update(book_review=data.get('book_review'), rating=data.get('rating'),
                                                     )
            return Response({"status":"sucess"}, status=200)
        except Exception as e:
            return Response({"status":"failure", "message":str(e)}, status=500)
