physical_activity_dict = {'walking': ['walk', 'walking', 'walking_for_exercise', 'lawn walking', 'lawn moving', 'lawn mowing', 'lawn',
                                      'walking for exercise'],
                             'cycling': ['cycle', 'cycling', 'bicycling'],
                             'running': ['run', 'running'],
                             'swimming': ['swim', 'swimming', 'lap swimming', 'seasonal swimming'],
                             'jogging': ['jogging', 'jogg'],
                             'gym': ['gym', 'gymming'],
                             'dancing': ['dance', 'dancing', 'kathak', 'zumba'],
                             'exercise': ['exercise'],
                             'lower_intensity_exercise': ['lower intensity exercise'],
                             'aerobic_exercise': ['aerobic exercise', 'other aerobic exercise'],
                             'yoga': 'yoga',
                             'playing': ['badminton', 'tennis', 'throw ball', 'ball'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                             'no_physical_activities': ['no_physical_activities', 'no physical activities'],
                             'data_not_available': ['data not available', 'data_not_available']
                             }

diet_dict = {'vegetarian': 'vegetarian',
             'vegan': 'vegan',
             'non_vegetarian': ['non-vegetarian', 'non vegetarian', 'non_vegetarian'],
             'ovo_vegetarian': ['ovo-vegetarian', 'ovo vegetarian', 'ovo_vegetarian'],
             'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
             'data_not_available': ['data not available', 'data_not_available', 'data not in report']
             }

menopause_status_dict = {'pre_menopausal': ['pre-menopausal', 'premenopausal'],
                         'post_menopausal': ['post-menopausal', 'post-menopause', 'post menopausal'],
                         'peri_menopausal': 'peri-menopausal',
                         'hysterectomy': ['hysterectomy', 'hysterctomy', 'post hysterectomy', 'hysterectome',
                                         'post -menopausal(hysterectomy done in 2012)'],
                        'oopherectomy': ['oophorectomy', 'bilateral oopherectomy'],
                        'other': 'male',
                        'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                        'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                         }

age_at_menopause_yrs_dict = {'NA': ['pre-menopausal', 'peri-menopausal', 'hysterectomy', 'bilateral oopherectomy',
                                    'male', 'hysterectome', '54 (Hysterectomy done)', '44 (Hysterectomy done in 2012)'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                            }


current_breast_cancer_detected_by_dict = {'self': 'self',
                                          'physician': 'physician',
                                          'routine_checkup': 'Annual body check up',
                                          'screening_camp': ['Screening Camp ID NA', 'Screening Camp ID 1',
                                                             'Screening Camp ID Data not in Report',
                                                             'Screening Camp ID Requires Follow-up'],
                                          'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                                 'requires follow up'],
                                          'data_not_available': ['data not available', 'data_not_available',
                                                                 'data not in report']
                                          }

rb_lb_symptoms_dict = {'lumps':['lumps','lump'],
                    'nipple_retraction':'nipple retraction',
                    'nipple_discharge': 'nipple discharge',
                    'pain_or_tenderness': 'pain or tenderness',
                    'dimpling':'dimpling',
                    'discolouration':['discolouration','redness'],
                    'ulceration':'ulceration',
                     'eczema':'eczema',
                    'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                    'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                    }

patient_metastasis_symptoms_dict = {'weight_loss': 'weight loss',
                                    'cough': 'cough',
                                    'bone_pain': 'bone pain',
                                    'headache':'headache',
                                    'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                           'requires follow up'],
                                    'data_not_available': ['data not available', 'data_not_available',
                                                           'data not in report']
                                    }


def column_names_info(db_column_name):
    patient_info_col_values_dict = 'NA'
    if db_column_name == 'type_physical_activity':
        patient_info_col_values_dict = {'walking': ['walk', 'walking', 'walking_for_exercise', 'lawn walking', 'lawn moving', 'lawn mowing', 'lawn',
                                      'walking for exercise'],
                             'cycling': ['cycle', 'cycling', 'bicycling'],
                             'running': ['run', 'running'],
                             'swimming': ['swim', 'swimming', 'lap swimming', 'seasonal swimming'],
                             'jogging': ['jogging', 'jogg'],
                             'gym': ['gym', 'gymming'],
                             'dancing': ['dance', 'dancing', 'kathak', 'zumba'],
                             'exercise': ['exercise'],
                             'lower_intensity_exercise': ['lower intensity exercise'],
                             'aerobic_exercise': ['aerobic exercise', 'other aerobic exercise'],
                             'yoga': 'yoga',
                             'playing': ['badminton', 'tennis', 'throw ball', 'ball'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                             'no_physical_activities': ['no_physical_activities', 'no physical activities'],
                             'data_not_available': ['data not available', 'data_not_available']
                             }
    elif db_column_name == 'diet':
        patient_info_col_values_dict = {'vegetarian': 'vegetarian',
             'vegan': 'vegan',
             'non_vegetarian': ['non-vegetarian', 'non vegetarian', 'non_vegetarian'],
             'ovo_vegetarian': ['ovo-vegetarian', 'ovo vegetarian', 'ovo_vegetarian'],
             'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
             'data_not_available': ['data not available', 'data_not_available', 'data not in report']
             }
    elif db_column_name == 'menopause_status':
        patient_info_col_values_dict = {'pre_menopausal': ['pre-menopausal', 'premenopausal'],
                         'post_menopausal': ['post-menopausal', 'post-menopause', 'post menopausal'],
                         'peri_menopausal': 'peri-menopausal',
                         'hysterectomy': ['hysterectomy', 'hysterctomy', 'post hysterectomy', 'hysterectome',
                                         'post -menopausal(hysterectomy done in 2012)'],
                        'oopherectomy': ['oophorectomy', 'bilateral oopherectomy'],
                        'other': 'male',
                        'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                        'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                         }
    elif db_column_name == 'age_at_menopause_yrs':
        patient_info_col_values_dict = {'NA': ['pre-menopausal', 'peri-menopausal', 'hysterectomy', 'bilateral oopherectomy',
                                    'male', 'hysterectome', '54 (Hysterectomy done)', '44 (Hysterectomy done in 2012)'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                            }

    elif db_column_name == 'current_breast_cancer_detected_by':
        patient_info_col_values_dict = {'self': 'self',
         'physician': 'physician',
         'routine_checkup': 'Annual body check up',
         'screening_camp': ['Screening Camp ID NA', 'Screening Camp ID 1',
                            'Screening Camp ID Data not in Report',
                            'Screening Camp ID Requires Follow-up'],
         'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                'requires follow up'],
         'data_not_available': ['data not available', 'data_not_available',
                                'data not in report']
         }
    elif db_column_name == 'rb_symptoms':
        patient_info_col_values_dict = {'lumps': ['lumps', 'lump'],
         'nipple_retraction': 'nipple retraction',
         'nipple_discharge': 'nipple discharge',
         'pain_or_tenderness': 'pain or tenderness',
         'dimpling': 'dimpling',
         'discolouration': ['discolouration', 'redness'],
         'ulceration': 'ulceration',
         'eczema': 'eczema',
         'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
         'data_not_available': ['data not available', 'data_not_available', 'data not in report']
         }
    elif db_column_name == 'lb_symptoms':
        patient_info_col_values_dict = {'lumps': ['lumps', 'lump'],
         'nipple_retraction': 'nipple retraction',
         'nipple_discharge': 'nipple discharge',
         'pain_or_tenderness': 'pain or tenderness',
         'dimpling': 'dimpling',
         'discolouration': ['discolouration', 'redness'],
         'ulceration': 'ulceration',
         'eczema': 'eczema',
         'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
         'data_not_available': ['data not available', 'data_not_available', 'data not in report']
         }
    elif db_column_name == 'patient_metastasis_symptoms':
        patient_info_col_values_dict = {'weight_loss': 'weight loss',
                                    'cough': 'cough',
                                    'bone_pain': 'bone pain',
                                    'headache':'headache',
                                    'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                           'requires follow up'],
                                    'data_not_available': ['data not available', 'data_not_available',
                                                           'data not in report']
                                    }
    return patient_info_col_values_dict

