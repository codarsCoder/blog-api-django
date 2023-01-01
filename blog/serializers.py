
from rest_framework import serializers
from .models import Category, Blog

class BlogSerializer(serializers.ModelSerializer):
    
    category = serializers.StringRelatedField() # read_only
    category_id = serializers.IntegerField()
    # user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Blog
        fields = ["id","title", "content","status", "category", "category_id"]
       
        

    def create(self, validated_data):
        
     validated_data["user_id"] =self.context["request"].user.id    ##hangi user göndermiş onu alıp create metodunu overrride ettik 
     return super().create(validated_data)
 
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
        