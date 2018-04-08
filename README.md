# DRF-quickstart
django-rest-framework quickstart tutorial

#根据django-rest-framework官方文档快速入门教程制作resful api
#安装pipenv虚拟环境
pip install pipenv
#创建虚拟环境
mkdir MY_DRF
cd MY_DRF
pipenv install django
pipenv install djangorestframework
#进入虚拟环境
pipenv shell

django-admin.py startproject MY_DRF
python manage.py startapp myapp

创建models
迁移数据仓库
python manage.py makemigrations
python manage.py migrate

序列化 在myapp中新建serializers.py
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        
视图 views.py 继承ModelViewSet类
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all().order_by('-created')
    serializer_class = MusicSerializer
    
配置 URLCONF

使用：
git clone https://github.com/YellowDong/DRF-quickstart.git
cd MY_DRF
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
用postman对api进行CRUD检查

