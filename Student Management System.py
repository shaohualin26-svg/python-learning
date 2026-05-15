
id = 1
student_info=[]
def add_name():
#正则模式：^表示开头，$表示结尾,[\u4e00-\u9fa5]表示匹配任意中文字符，\s表示匹配任意空白字符，+表示匹配任意空白字符一次或者多次

    pattern=r'^[\u4e00-\u9fa5]+$'
    while True:
        name=input('请输入学生名字')
        # 匹配名字是否为符合中文字符，是的话就将名字赋给name变量
        import re
        if re.match(pattern,name):
            break
        else:
            print('名字不合规，请输入正确的名字')
    return  name

def add_age():
    while True:
        try:
            age=int(input('请输入年龄'))
            if age<0 or age>120:
                print('请输入正确的年龄')
                continue
        except ValueError:
            print('请输入整数数字')
        else:
            break
    return age
def add_sex():
    while True:
        try:
            sex=input('请输入性别')
            if sex!='男' and sex!='女':
                print('请输入正确的性别')
                continue
        except ValueError:
            print('请输入男或女')
        else:
            break
    return sex
def add_score():
    while True:
        try:
            score=int(input('请输入分数'))
            if score<0 or score>100:
                print('请输入正确的分数')
                continue
        except ValueError:
            print('请输入整数数字')
        else:
            break
    return score
def set_id():
        while True:
            try:
                id_student = int(input('请输入你的id'))
                if id_student < 0:
                    print('请输入正确的id')
                    continue
            except ValueError:
                print('请输入整数数字')
            else:
                break
        return id_student
# 加
def add_student_info():
    global id
    name=add_name()
    age=add_age()
    sex=add_sex()
    score=add_score()
    stu= {
        'id':id,
        '姓名':name,
        '年龄':age,
        '性别' :sex,
        '分数':score
    }
    id+=1
    student_info.append(stu)
    print(f'添加成功，学生列表为{student_info}')
# 展现
def show_student_info():
    for item in student_info:
        print(f'id:{item["id"]},姓名:{item["姓名"]},年龄：{item["年龄"]},性别：{item["性别"]},分数{item["分数"]}\n')
# 删
def delete_student_info():
    id_student=set_id()
    for item in student_info:
        if item['id']==id_student:
            student_info.remove(item)
            print(f'删除成功，现在的学生列表为{student_info}')
            return
# 修改
def update_student_info():
    id_input =set_id()


    for item in student_info:
        if item['id'] == id_input:
            item['姓名']=add_name()
            item['年龄']=add_age()
            item['性别']=add_sex()
            item['分数']=add_score()
            print(f'修改成功，当前学生的列表为{student_info}')


# 排序
def sort_student_info():
    def keyFunc(data):
        return  data['分数']
    student_info.sort(key=keyFunc,reverse=True)
    print(f'排序成功，当前的学生列表为{student_info}')


    pass
def run_main():
    while True:
        print("\n" + "*" * 45)
        print("\t\tLin设计学生管理系统 2.0版")
        print("*" * 45)
        print("\t【1】 添加学生信息")
        print("\t【2】 展现学生信息")
        print("\t【3】 删除学生信息")
        print("\t【4】 修改学生信息")
        print("\t【5】 展示全部并排序所有学生")
        print("\t【6】 退出管理系统")
        print("*" * 45)
        choice=input('请输入你的选项')
        if choice=='1':
            add_student_info()
        elif choice=='2':
            show_student_info()
        elif choice=='3':
            delete_student_info()
        elif choice=='4':
            update_student_info()
        elif choice=='5':
            sort_student_info()
        elif choice=='6':
           break
        else:
            print("请输入正确的选项")

run_main()