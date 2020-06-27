input_columns = [
    'sex','age','disease', 'pre_hospitalization_status','days','family','helper','motivation','meal','hygienic','wipingClean','upperBodyDressing','lowerBodyDressing',
    'toiletAction','urinationControl','defecationControl','bedsChairsWheelchairs','toilet','bathtubShower','walkingWheelchair',
    'stairs','understanding','expression','socialCommunication','problemSolving','memory',
]

attributes = ['sex','age','disease', 'pre_hospitalization_status','days','family','helper','motivation']

column_current =['meal','hygienic','wipingClean','upperBodyDressing','lowerBodyDressing','toiletAction','urinationControl','defecationControl',
            'bedsChairsWheelchairs','toilet','bathtubShower','walkingWheelchair','stairs','understanding','expression',
            'socialCommunication','problemSolving','memory']
            
column_current_ja = ['食事','整容','清拭','更衣上半身','更衣下半身','トイレ動作','排尿管理','排便管理','ベッド,椅子<br>,車椅子移乗','トイレ移乗',
                    '浴槽,<br>シャワー移乗','歩行,車椅子','階段','理解','表出','社会的交流','問題解決','記憶']


column_afters =[
    ['discharge'],
    ['meal_after_1M','hygienic_after_1M','wipingClean_after_1M','upperBodyDressing_after_1M','lowerBodyDressing_after_1M','toiletAction_after_1M','urinationControl_after_1M',
    'defecationControl_after_1M','bedsChairsWheelchairs_after_1M','toilet_after_1M','bathtubShower_after_1M','walkingWheelchair_after_1M',
    'stairs_after_1M','understanding_after_1M','expression_after_1M','socialCommunication_after_1M','problemSolving_after_1M','memory_after_1M'],
    ['meal_after_2M','hygienic_after_2M','wipingClean_after_2M','upperBodyDressing_after_2M','lowerBodyDressing_after_2M',
    'toiletAction_after_2M','urinationControl_after_2M','defecationControl_after_2M','bedsChairsWheelchairs_after_2M','toilet_after_2M',
    'bathtubShower_after_2M','walkingWheelchair_after_2M','stairs_after_2M','understanding_after_2M','expression_after_2M','socialCommunication_after_2M',
    'problemSolving_after_2M','memory_after_2M'],
    ['meal_after_3M','hygienic_after_3M','wipingClean_after_3M','upperBodyDressing_after_3M','lowerBodyDressing_after_3M',
    'toiletAction_after_3M','urinationControl_after_3M','defecationControl_after_3M','bedsChairsWheelchairs_after_3M','toilet_after_3M',
    'bathtubShower_after_3M','walkingWheelchair_after_3M','stairs_after_3M','understanding_after_3M','expression_after_3M','socialCommunication_after_3M',
    'problemSolving_after_3M','memory_after_3M']
    ]


# predict colums 
sum_1M = ['meal_after_1M','hygienic_after_1M','wipingClean_after_1M','upperBodyDressing_after_1M','lowerBodyDressing_after_1M','toiletAction_after_1M','urinationControl_after_1M',
    'defecationControl_after_1M','bedsChairsWheelchairs_after_1M','toilet_after_1M','bathtubShower_after_1M','walkingWheelchair_after_1M',
    'stairs_after_1M','understanding_after_1M','expression_after_1M','socialCommunication_after_1M','problemSolving_after_1M','memory_after_1M'
]
sum_2M = ['meal_after_2M','hygienic_after_2M','wipingClean_after_2M','upperBodyDressing_after_2M','lowerBodyDressing_after_2M',
    'toiletAction_after_2M','urinationControl_after_2M','defecationControl_after_2M','bedsChairsWheelchairs_after_2M','toilet_after_2M',
    'bathtubShower_after_2M','walkingWheelchair_after_2M','stairs_after_2M','understanding_after_2M','expression_after_2M','socialCommunication_after_2M',
    'problemSolving_after_2M','memory_after_2M'
    ]

sum_3M =['meal_after_3M','hygienic_after_3M','wipingClean_after_3M','upperBodyDressing_after_3M','lowerBodyDressing_after_3M',
    'toiletAction_after_3M','urinationControl_after_3M','defecationControl_after_3M','bedsChairsWheelchairs_after_3M','toilet_after_3M',
    'bathtubShower_after_3M','walkingWheelchair_after_3M','stairs_after_3M','understanding_after_3M','expression_after_3M','socialCommunication_after_3M',
    'problemSolving_after_3M','memory_after_3M'
]

fim_motor_item =['meal','hygienic','wipingClean','upperBodyDressing','lowerBodyDressing','toiletAction','urinationControl','defecationControl',
            'bedsChairsWheelchairs','toilet','bathtubShower','walkingWheelchair','stairs'
]