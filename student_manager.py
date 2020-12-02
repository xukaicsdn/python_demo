import random

"""
    数据模型类：StudentModel
        数据：编号 id,姓名 name ,年龄 age
    逻辑控制类：StudentManagerController
        数据：学生列表 __stu_list
        行为：获取列表stu_list,添加学生add_student,删除学生
            del_student,修改学生update_student,根据成绩排序
            order_by_score
    界面视图类：StudentManagerView
        数据;逻辑控制对象__manager
        行为：显示菜单__dispaly_menu,选择菜单项__select_menu

输入学生__input_students,输出学生__output_students,删除学生
修改学生信息__modify_student,按成绩输出学生__output_student
"""


# 练习1:创建学生数据模型类.
# 练习2:创建逻辑控制类
#          数据:学生列表__stu_list.
#          行为:获取列表的只读属性stu_list,
#              添加学生方法add_student.

class StudentModel:
    """
        学生数据模型类
    """

    def __init__(self,name="",age=0,score=0,id=0):
        """
            创建学生对象
        :param id:
        :param name:
        :param age:
        :param score:
        :return:
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        self.__score = value






class StudentManagerController:
    """
        学生逻辑控制器
    """
    def __init__(self):
       self. __list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu[:]

    def add_student(self,stu):
        """
            添加新学生
        :param stu: 需要添加的学生对象
        :return:
        """

        stu.id = self.__generate_id()
        self.__list_stu.append(stu)

    def __generate_id(self):
        # 生成编号的需求:新编号,比上次添加的对象编号多1
        if len(self.__list_stu) > 0:
            id = self.__list_stu[-1].id + 1
        else:
            id = 1
        return int(id)

    def update_student(self,stu):
        """
            更新学生信息,体会内存图
        :param stu:
        :return:
        """
        for item in self.__list_stu:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
        return False

        # 不对     好好提体会体会内存图   很重要   参考孙悟空内存图
        # item是每个学生对象变量的内存地址
        # for item in self.__list_stu:
        #         if item.id == stu.id:
                      # 这样把学生对象指针变了，背离修改学生信息的需求了，列表里存的是学生对象的内存地址
        #             item = stu



    def order_by_score(self):
        """
            根据成绩升序排序
            list_stu = [
            Student("zs","男",95,10),
            Student("ls","女",25,60),
            Student("ww","男",58,30),
            Student("zl","女",65,50)
            ]
        :return:
        """

        # 为了不影响以前的列表顺序  切片处理
        new_list = self.__list_stu[:]
        for r in range(len(new_list) - 1):
            for c in range(r + 1,len(new_list)):
                if new_list[r].scoer > new_list[c].score:
                    new_list[r],new_list[c] = new_list[c],new_list[r]
        return new_list

    def remove_student(self,id):
        for stu in self.list_stu:
            if stu.id == id:
                self.list_stu.remove(stu)
                return True
        return False


# controller = StudentManagerController()
# controller.add_student(StudentModel("zs",18,85))
#
# for item in controller.list_stu:
#     print(item.id,item.name,item.age,item.score)



class StudentManagerView:
    """
        界面视图类
    """
    def __init__(self):
        #创建逻辑控制器对象
        self.__manager = StudentManagerController()

    def __input_students(self):
        #1.在控制台中录入学生信息,存成学生对象StudentModel.
        stu = StudentModel()
        stu.name = str(input("请录入学生姓名："))
        stu.age = int(input("请录入学生年龄："))
        stu.score = int(input("请录入学生成绩："))

        #2.调用逻辑控制器的add_student方法
        self.__manager.add_student(stu)

        for item in self.__manager.list_stu:
            print(item.id,item.name,item.age)


    def __output_students(self,list_target):
        """
            显示学生列表信息
        :return:
        """
        # for stu in self.__manager.list_stu:
        for stu in list_target:
            print("%d -- %s -- %d -- %d"%(stu.id,stu.name,stu.age,stu.score))

    def __output_student_by_score(self):
        """
            根据成绩倒序排序
        :return:
        """

        # 排序逻辑不应该放到这，应该放到逻辑里面 ，因为这只负责显示页面
        list_target = self.__manager.order_by_score()
        self.__output_students(list_target)

    def __delete_student(self):
        id = int(input ("请输入需要删除的学生编号:"))
        if self.__manager.remove_student(id):
            print("删除学生成功")
        else:
            print("删除学生失败")


    def __modify_student(self):
        """
            修改学生信息
        :return:
        """
        stu = StudentModel()
        stu.id = int(input ("请输入需要修改的学生编号:"))
        stu.name = input("请输入姓名")
        stu.age = int(input("请输入年龄"))
        stu.score = int(input("请输入成绩"))
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("更新失败")





    # 1.显示菜单    私有方法，类外边不让调用
    def __display_menu(self):
        """
            显示菜单
        :return:
        """
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修政学生")
        print("5)按照成绩降序排列")

    # 2.选择菜单
    def __select_menu(self):
        """
            选择菜单
        :return:
        """
        number = input("请输入选项：")
        if number == "1":
            self.__input_students()
        elif number =="2":
            self.__output_students(self.__manager.list_stu)
        elif number =="3":
            self.__delete_student()
        elif number =="4":
            self.__modify_student()
        elif number =="5":
            self.__output_student_by_score()

    def main(self):
        """
            界面入口方法
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()


view = StudentManagerView()
view.main()



# 练习3:按2键显示所有学生信息。
# 练习4:按5键,根据成绩升序显示所有学生信息


