from rest_framework import serializers
from . import models

class RegisterModelSerializer(serializers.ModelSerializer):
    # 自定义反序列化字段的规则必须在字段声明时规定
    # 设置员工编号
    # emp_num = serializers.IntegerField()

    class Meta:
        model = models.Emp
        fields = ('id','name', 'emp_num')

    def create(self, validated_data):

        username = validated_data.get('username')
        password = validated_data.get('password')
        return models.User.objects.create_user(username=username,password=password)


from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.serializers import jwt_encode_handler


class LoginModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['username', 'password']
        extra_kwargs = {
            'username': {
                'read_only': True
            },

        }

    def validate(self, attrs):
        print(attrs,'0009')
        username = attrs.get('username')
        password = attrs.get('password')
        print(username,password)
        # 多方式登录：各分支处理得到该方式下对应的用户
        user_obj = models.User.objects.filter(username=username).first()
        print(user_obj)

        # 签发：得到登录用户，签发token并存储在实例化对象中
        if user_obj and user_obj.check_password(password):
            # 签发token，将token存放到 实例化类对象的token 名字中
            payload = jwt_payload_handler(user_obj)
            token = jwt_encode_handler(payload)
            # 将当前用户与签发的token都保存在序列化对象中
            self.user = user_obj
            self.token = token
            return attrs

        raise serializers.ValidationError({'data': '数据有误'})

# 员工分类 好像忘写 type


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Emp
        fields = ('id', 'group_name','emp_num')

# 员工


class EmpModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Org
        fields = ('id', 'name','type')