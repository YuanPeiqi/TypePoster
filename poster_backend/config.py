font_path_global = {'bold': 'C:\\Windows\\Fonts\\msyhbd.ttc', 'normal': 'C:\\Windows\\Fonts\\msyh.ttc'}

font_shift = 10

CONTENT_TYPE = ['non-leaf', 'padding', 'title', 'abstract', 'introduction', 'info', 'logo', 'photo']

English2Chinese = {'time': '时间:', 'location': '地点:', 'reporter': '报告人:', 'inviter': '邀请人:',
                   'meeting_num': '腾讯会议号:', 'abstract': '报告摘要', 'introduction': '报告人简介'}

style_list = {
    'business_1': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/business_1.png',
            # 'opacity': 0.8,
            'opacity': 1
        },
        'rect': {'backgroundColor': '#f1f2f6', 'opacity': 0.7},
        'info': {'fontSize': '0px', 'color': '#2f3542', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#2f3542', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#2D5960', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'business_2': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/business_2.png',
            # 'opacity': 0.9
            'opacity': 1
        },
        'rect': {'backgroundColor': '#f1f2f6', 'opacity': 0.6},
        'info': {'fontSize': '0px', 'color': '#2f3542', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#2f3542', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#2D5960', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'business_3': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/business_3.png',
            'opacity': 1
            # 'opacity': 0.8
        },
        'rect': {'backgroundColor': '#f1f2f6', 'opacity': 0.5},
        'info': {'fontSize': '0px', 'color': '#2f3542', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#2f3542', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#2D5960', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#2f3640', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'business_4': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/business_4.png',
            'opacity': 1
            # 'opacity': 0.85
        },
        'rect': {'backgroundColor': '#f1f2f6', 'opacity': 0.7},
        'info': {'fontSize': '0px', 'color': '#2f3542', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#2f3542', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#2D5960', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'business_5': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/business_5.png',
            'opacity': 1
            # 'opacity': 0.6
        },
        'rect': {'backgroundColor': '#4b4b4b', 'opacity': 0.4},
        'info': {'fontSize': '0px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#ffa502', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#f1f2f6', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#ffa502', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#ffffff', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'tech_1': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/tech_1.png',
            'opacity': 1
            # 'opacity': 0.8
        },
        'rect': {'backgroundColor': '#f1f2f6', 'opacity': 0.7},
        'info': {'fontSize': '0px', 'color': '#2f3542', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#2f3542', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#2D5960', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'tech_2': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/tech_2.png',
            'opacity': 1
            # 'opacity': 0.8
        },
        'rect': {'backgroundColor': '#dfe4ea', 'opacity': 0.4},
        'info': {'fontSize': '0px', 'color': '#2f3542', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#2f3542', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#2D5960', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'tech_3': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/tech_3.png',
            'opacity': 1
            # 'opacity': 0.9
        },
        'rect': {'backgroundColor': '#4b4b4b', 'opacity': 0.4},
        'info': {'fontSize': '0px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#ffa502', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#ffffff', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#ffa502', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#ffffff', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'tech_4': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/tech_4.png',
            'opacity': 1
            # 'opacity': 0.8
        },
        'rect': {'backgroundColor': '#4b4b4b', 'opacity': 0.4},
        'info': {'fontSize': '0px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#ffa502', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#ffffff', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#ffa502', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#ffffff', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'chemistry_1': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/chemistry_1.png',
            'opacity': 1
            # 'opacity': 0.9
        },
        'rect': {'backgroundColor': '#dfe4ea', 'opacity': 0.3},
        'info': {'fontSize': '0px', 'color': '#2f3542', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#2f3542', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#2D5960', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#FFFFFF', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'chemistry_2': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/chemistry_2.png',
            'opacity': 1
            # 'opacity': 0.8
        },
        'rect': {'backgroundColor': '#dfe4ea', 'opacity': 0.4},
        'info': {'fontSize': '0px', 'color': '#2f3542', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#2f3542', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#2D5960', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'earth_1': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/earth_1.png',
            'opacity': 1
            # 'opacity': 0.9
        },
        'rect': {'backgroundColor': '#4b4b4b', 'opacity': 0.4},
        'info': {'fontSize': '0px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#ffa502', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#f1f2f6', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#ffa502', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#ffffff', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'chip_1': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/chip_1.png',
            'opacity': 1
            # 'opacity': 0.8
        },
        'rect': {'backgroundColor': '#4b4b4b', 'opacity': 0.4},
        'info': {'fontSize': '0px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#ffa502', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#f1f2f6', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#ffa502', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#ffffff', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'chip_2': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/chip_2.png',
            'opacity': 1
            # 'opacity': 0.8
        },
        'rect': {'backgroundColor': '#4b4b4b', 'opacity': 0.4},
        'info': {'fontSize': '0px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#ffa502', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#ffffff', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#ffa502', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#ffffff', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'cs_1': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/cs_1.png',
            'opacity': 1
            # 'opacity': 0.7
        },
        'rect': {'backgroundColor': '#4b4b4b', 'opacity': 0.6},
        'info': {'fontSize': '0px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#ffa502', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#ffffff', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#ffa502', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#ffffff', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'AI_1': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/AI_1.png',
            'opacity': 1
            # 'opacity': 0.8
        },
        'rect': {'backgroundColor': '#4b4b4b', 'opacity': 0.6},
        'info': {'fontSize': '0px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#ffa502', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#ffffff', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#ffa502', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#ffffff', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'bioscience_2': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/bioscience_2.png',
            'opacity': 1
            # 'opacity': 0.5
        },
        'rect': {'backgroundColor': '#f1f2f6', 'opacity': 0.6},
        'info': {'fontSize': '0px', 'color': '#2f3542', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#2f3542', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#2D5960', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#2D5960', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'bioscience_3': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/bioscience_3.png',
            'opacity': 1
            # 'opacity': 0.8
        },
        'rect': {'backgroundColor': '#4b4b4b', 'opacity': 0.4},
        'info': {'fontSize': '0px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#ffa502', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#f1f2f6', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#ffa502', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#ffffff', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
    'bioscience_4': {
        'background': {
            'url': 'http://localhost:5000/get_background/test_user/bioscience_4.png',
            'opacity': 1
            # 'opacity': 0.8
        },
        'rect': {'backgroundColor': '#4b4b4b', 'opacity': 0.3},
        'info': {'fontSize': '0px', 'color': '#f1f2f6', 'fontWeight': 'bold', 'textAlign': 'left',
                 'letterSpacing': 0, 'lineHeight': '100%'},
        'info_title': {'fontSize': '0px', 'color': '#ffa502', 'fontWeight': 'bold', 'textAlign': 'left',
                       'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '100%'},
        'ab&intro': {'fontSize': '14px', 'fontFamily': '', 'color': '#f1f2f6', 'fontWeight': 'bold',
                     'textAlign': 'left', 'fontStyle': '', 'letterSpacing': 0, 'lineHeight': '135%'},
        'ab&intro_title': {'fontSize': '19px', 'fontFamily': '', 'color': '#ffa502', 'fontWeight': 'bold',
                           'textAlign': 'left', 'letterSpacing': 0, 'lineHeight': '100%'},
        'title': {'fontSize': '34px', 'color': '#ffffff', 'fontWeight': 'bold', 'textAlign': 'left',
                  'letterSpacing': 0, 'lineHeight': '150%'}
    },
}

hierarchical_layout_list = [
    {
        'id': 0,
        'preview': '',
        'description': '模板',
        'layout_file': 'template0.lay',
        'hover': False,
        'data': [
            {'type': "background"},
            {'type': "rect", 'rect_type': 'abstract', 'w': 646, 'h': 220, 'x': 17, 'y': 443, 'content': []},
            {'type': "rect", 'rect_type': 'introduction', 'w': 646, 'h': 220, 'x': 17, 'y': 673, 'content': []},
            {'type': "rect", 'rect_type': 'info', 'w': 465, 'h': 210, 'x': 198, 'y': 213, 'content': []},
            {'type': "rect", 'rect_type': 'divider', 'w': 646, 'h': 4, 'x': 17, 'y': 666,
             'backgroundColor': '#4b4b4b', 'opacity': 1, 'content': []},
            {'type': "img", 'img_type': 'customized_logo', 'w': 265, 'h': 55, 'x': 390, 'y': 17},
            {'type': "img", 'img_type': 'logo', 'w': 212, 'h': 55, 'x': 17, 'y': 17},
            {'type': "img", 'img_type': 'photo', 'w': 160, 'h': 210, 'x': 17, 'y': 214},
            {'type': "img", 'img_type': 'qrcode', 'w': 106, 'h': 106, 'x': 542, 'y': 300},
            {'type': "title", 'content': '', 'w': 612, 'h': 120, 'x': 34, 'y': 76, },
        ]
    },
    {
        'id': 1,
        'preview': '',
        'description': '模板',
        'layout_file': 'template1.lay',
        'hover': False,
        'data': [
            {'type': "background"},
            {'type': "rect", 'rect_type': 'abstract', 'w': 646, 'h': 205, 'x': 17, 'y': 320, 'content': []},
            {'type': "rect", 'rect_type': 'introduction', 'w': 646, 'h': 350, 'x': 17, 'y': 540, 'content': []},
            {'type': "rect", 'rect_type': 'info', 'w': 480, 'h': 136, 'x': 180, 'y': 170, 'content': []},
            {'type': "img", 'img_type': 'customized_logo', 'w': 265, 'h': 55, 'x': 390, 'y': 10},
            {'type': "img", 'img_type': 'logo', 'w': 212, 'h': 55, 'x': 10, 'y': 10},
            {'type': "img", 'img_type': 'photo', 'w': 150, 'h': 230, 'x': 17, 'y': 76},
            {'type': "img", 'img_type': 'qrcode', 'w': 106, 'h': 106, 'x': 542, 'y': 190},
            {'type': "title", 'content': '', 'w': 460, 'h': 80, 'x': 180, 'y': 76},
        ]
    },
    {
        'id': 2,
        'preview': '',
        'description': '模板',
        'layout_file': 'template2.lay',
        'hover': False,
        'data': [
            {'type': "background"},
            {'type': "rect", 'rect_type': 'abstract', 'w': 646, 'h': 200, 'x': 17, 'y': 320, 'contenet': []},
            {'type': "rect", 'rect_type': 'introduction', 'w': 646, 'h': 350, 'x': 17, 'y': 540, 'contenet': []},
            {'type': "rect", 'rect_type': 'info', 'w': 480, 'h': 146, 'x': 17, 'y': 160, 'contenet': []},
            {'type': "img", 'img_type': 'customized_logo', 'w': 265, 'h': 55, 'x': 390, 'y': 10},
            {'type': "img", 'img_type': 'logo', 'w': 212, 'h': 55, 'x': 10, 'y': 10},
            {'type': "img", 'img_type': 'photo', 'w': 150, 'h': 230, 'x': 510, 'y': 76},
            {'type': "img", 'img_type': 'qrcode', 'w': 106, 'h': 106, 'x': 375, 'y': 190},
            {'type': "title", 'content': '', 'w': 460, 'h': 60, 'x': 17, 'y': 76}
        ]
    }
]
