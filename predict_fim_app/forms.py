from django import forms


#1
sex=[
   (1,"男性"),
   (2,"女性")
]
#2
age=[70]

#3
disease=[
   (1,"骨関節疾患"),
   (2,"脳血管疾患"),
   (3,"廃用症候群"),
   (4,"その他")
]

#4
pre_hospitalization_status = （
    (1,"自立"),
    (2,"要支援1"),
    (3,"要支援2"),
    (4,"要介護1"),
    (5,"要介護2"),
    (6,"要介護3"),
    (7,"要介護4"),
    (8,"要介護5"),
）

days = (
   (1,"1週間"),
   (2,"2週間"),
   (3,"3週間"),
   (4,"4週間"),
   (5,"5週間"),
   (6,"6週間"),
   (7,"7週間"),
   (8,"8週間"),
   (9,"9週間以上"),
)
family = [
    (1,"独居"),
    (2,"日中独居"),
    (3,"同居"),
    (4,"その他")
]

#5
helper=[
   (0,"無し"),
   (1,"有り")
]

motivation = [
    (1,"とてもある"),
    (2,"少しある"),
    (3,"あまりない"),
    (4,"全くない")
]


#6
meal=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]

#7
hygienic=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#8
wipingClean=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#9
upperBodyDressing=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#10
lowerBodyDressing=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#11
toiletAction=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#12
urinationControl=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#13
defecationControl=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#14
bedsChairsWheelchairs=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#15
toilet=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#16
bathtubShower=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#17
walkingWheelchair=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#18
stairs=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#19
understanding=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#20
expression=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#21
socialCommunication=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#21
problemSolving=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]
#22
memory=[
    (1,'全介助'),
    (2,'最大介助'),
    (3,'中等度介助'),
    (4,'最小介助'),
    (5,'監視・準備'),
    (6,'修正自立'),
    (7,'完全自立')
]


class CareForm(forms.Form):

    
    sex = forms.ChoiceField(
        label='１：性別', choices=sex,
        required=True,initial=[1],
        widget=forms.RadioSelect)

    age = forms.IntegerField(
        label='２：年齢',
        required=True,initial=[70],
       )
    
    disease = forms.ChoiceField(
        label='3：疾患情報', choices=disease,
        required=True,initial=[2],
        widget=forms.RadioSelect)
    
    pre_hospitalization_status = forms.ChoiceField(
        label='４：病前の生活状態', choices=pre_hospitalization_status,
        required=True,initial=[1],
        widget=forms.Select)

    days = forms.ChoiceField(
        label='５：発症からの経過日数', choices=days,
        required=True,initial=[1],
        widget=forms.Select)

    
     family = forms.ChoiceField(
        label='６：家族構成', choices=family,
        required=True,initial=[1],
        widget=forms.RadioSelect)


    helper = forms.ChoiceField(
        label='７：主要介護者の有無', choices=helper,
        required=True,initial=[1],
        widget=forms.RadioSelect)

        
    motivation = forms.ChoiceField(
        label='８：リハ意欲', choices=motivation,
        required=True,initial=[1],
        widget=forms.RadioSelect)
    

    meal = forms.ChoiceField(
        label='９：食事', choices=meal,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    hygienic = forms.ChoiceField(
        label='１０：整容', choices=hygienic,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    wipingClean = forms.ChoiceField(
        label='１１：清拭', choices=wipingClean,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    upperBodyDressing = forms.ChoiceField(
        label='１２：更衣上半身', choices=upperBodyDressing,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    lowerBodyDressing = forms.ChoiceField(
        label='１３：更衣下半身', choices=lowerBodyDressing,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    toiletAction = forms.ChoiceField(
        label='１４：トイレ動作', choices=toiletAction,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    urinationControl = forms.ChoiceField(
        label='１５：排尿管理', choices=urinationControl,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    defecationControl = forms.ChoiceField(
        label='１６：排便管理', choices=defecationControl,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    bedsChairsWheelchairs = forms.ChoiceField(
        label='１７：ベッド・椅子・車椅子移乗', choices=bedsChairsWheelchairs,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    toilet = forms.ChoiceField(
        label='１８：トイレ移乗', choices=toilet,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    bathtubShower = forms.ChoiceField(
        label='１９：浴槽・シャワー移乗', choices=bathtubShower,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    walkingWheelchair = forms.ChoiceField(
        label='２０：歩行・車椅子', choices=walkingWheelchair,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    stairs = forms.ChoiceField(
        label='２１：階段', choices=stairs,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    understanding = forms.ChoiceField(
        label='２２：理解', choices=understanding,
        required=True,initial=[4],
        widget=forms.RadioSelect)
    
    expression = forms.ChoiceField(
        label='２３：表出', choices=expression,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    socialCommunication = forms.ChoiceField(
        label='２４：社会的交流', choices=socialCommunication,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    problemSolving = forms.ChoiceField(
        label='２５：問題解決', choices=problemSolving,
        required=True,initial=[4],
        widget=forms.RadioSelect)

    memory = forms.ChoiceField(
        label='２６：記憶', choices=memory,
        required=True,initial=[4],
        widget=forms.RadioSelect)