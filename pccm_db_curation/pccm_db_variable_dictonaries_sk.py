def column_names_info(db_column_name):
    col_values_dict = 'NA'
    if db_column_name == 'type_physical_activity':
        col_values_dict = {'walking': ['walk', 'walking', 'walking_for_exercise', 'lawn walking', 'lawn moving', 'lawn mowing', 'lawn',
                                      'walking for exercise'],
                             'cycling': ['cycle', 'cycling', 'bicycling'],
                             'running': ['run', 'running'],
                             'swimming': ['swim', 'swimming', 'lap swimming', 'seasonal swimming'],
                             'jogging': ['jogging', 'jogg'],
                             'gym': ['gym', 'gymming'],
                             'dancing': ['dance', 'dancing', 'kathak', 'zumba'],
                             'exercise': ['exercise'],
                             'lower_intensity_exercise': ['lower intensity exercise', 'lower intensity excercise',
                                                          'lower intensity excersise'],
                             'aerobic_exercise': ['aerobic exercise', 'other aerobic exercise'],
                             'yoga': 'yoga',
                             'sedentary': 'sedentary',
                             'playing': ['badminton', 'tennis', 'throw ball', 'ball'],
                             'NA' : ['na', 'no'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                             'no_physical_activities': ['no_physical_activities', 'no physical activities'],
                             'data_not_available': ['data not available', 'data_not_available', 'data not in report',
                                                    'data not in report ']
                             }

    elif db_column_name == 'diet':
        col_values_dict = {'vegetarian': 'vegetarian',
                            'vegan': 'vegan',
                            'non_vegetarian': ['non-vegetarian', 'non vegetarian', 'non_vegetarian'],
                            'ovo_vegetarian': ['ovo-vegetarian', 'ovo vegetarian', 'ovo_vegetarian'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                             }

    elif db_column_name == 'marital_status':
        col_values_dict = {'married': ['married', 'maried', 'marrird', 'marrried'],
                           'unmarried': ['unmarried', 'never married', 'single'],
                           'widow': ['widow', 'divorced'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                           }

    elif db_column_name == 'menopause_status':
        col_values_dict = {'pre_menopausal': ['pre-menopausal', 'premenopausal'],
                            'post_menopausal': ['post-menopausal', 'post-menopause', 'post menopausal'],
                            'peri_menopausal': 'peri-menopausal',
                            'hysterectomy': ['hysterectomy', 'hysterctomy', 'post hysterectomy', 'hysterectome',
                                         'post -menopausal(hysterectomy done in 2012)'],
                            'oopherectomy': ['oophorectomy', 'bilateral oopherectomy'],
                            'other': 'male',
                            'NA': 'na',
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                            }

    elif db_column_name == 'age_at_menopause_yrs':
        col_values_dict = {'NA': ['pre-menopausal', 'peri-menopausal', 'hysterectomy', 'bilateral oopherectomy',
                                    'male', 'hysterectome', '54 (Hysterectomy done)', '44 (Hysterectomy done in 2012)'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                            }

    elif db_column_name == 'success_fertility_treatment':
        col_values_dict = {'yes': 'pregnancy from treatment',
                           'no': ['not successful', 'no pregnancy from treatment', 'not succesful'],
                           'NA': ['na', 'no fertility treatment used'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up',
                                                  'require follow up'],
                           'data_not_available': ['data not available', 'data_not_available', 'data not in report',
                                                  'data not in report ']
                           }

    elif db_column_name == 'current_breast_cancer_detected_by':
        col_values_dict = {'self': 'self',
                            'physician': 'physician',
                            'routine_checkup': ['annual body check up', 'routine'],
                            'screening_camp': ['screening camp id na', 'screening camp id 1',
                                    'screening camp id data not in report',
                                    'screening camp id requires follow-up', 'screening camp id data not in Report',
                                               ],
                            'NA': 'na',
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available',
                                        'data not in report']
         }

    elif db_column_name == 'rb_symptoms':
        col_values_dict = {'lumps': ['lumps', 'lump'],
                            'nipple_retraction': 'nipple retraction',
                            'nipple_discharge': 'nipple discharge',
                            'pain_or_tenderness': 'pain or tenderness',
                            'dimpling': 'dimpling',
                            'discolouration': ['discolouration', 'redness'],
                            'ulceration': 'ulceration',
                            'eczema': 'eczema',
                            'NA': 'na',
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                   'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available',
                                                   'data not in report']
                            }

    elif db_column_name == 'lb_symptoms':
        col_values_dict = {'lumps': ['lumps', 'lump'],
                            'nipple_retraction': 'nipple retraction',
                            'nipple_discharge': 'nipple discharge',
                            'pain_or_tenderness': 'pain or tenderness',
                            'dimpling': 'dimpling',
                            'discolouration': ['discolouration', 'redness'],
                            'ulceration': 'ulceration',
                            'eczema': 'eczema',
                            'NA': 'na',
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                   'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available',
                                                   'data not in report']
                             }

    elif db_column_name == 'patient_metastasis_symptoms':
        col_values_dict = {'weight_loss': ['weight loss', 'weightloss'],
                                'cough': 'cough',
                                'bone_pain': 'bone pain',
                                'headache': 'headache',
                                'NA': ['na', 'no metastatis symptoms'],
                                'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                           'requires follow up'],
                                'data_not_available': ['data not available', 'data_not_available',
                                                           'data not in report']
                                }

    elif db_column_name == 'mammography':
        col_values_dict = {'yes': 'mammography done',
                           'no': 'mammography not done for diagnosis',
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'mammography_breast':
        col_values_dict = {'bilateral': 'bilateral',
                           'right_breast': ['right breast', 'right'],
                           'left_breast': ['left breast', 'left'],
                           'NA': ['na', 'mammography not done for diagnosis'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                        'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available',
                                                        'data not in report']
                            }

    elif db_column_name == 'mammography_massshape':
        col_values_dict = {'irregular': 'irregular',
                              'oval': ['oval', 'small ovoid'],
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'well_marginated': 'well marginated',
                              'lobulated': ['lobulated', 'lobulations'],
                              'microlobulated': ['microlobulated', 'macro-lobulated'],
                              'ill_defined': ['illdefined', 'ill defined', 'ill', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'indistinct_margins': ['indistinct', 'indistinct margins'],
                              'oblong': 'oblong',
                              'invasive': 'invasive',
                              'NA': ['na', 'mammography not done for diagnosis', 'nan'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
                              }

    elif db_column_name == 'mammography_massmargin':
        col_values_dict = {'irregular': 'irregular',
                              'oval': ['oval', 'small ovoid'],
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'well_marginated': 'well marginated',
                              'lobulated': ['lobulated', 'lobulations'],
                              'microlobulated': ['microlobulated', 'macro-lobulated'],
                              'ill_defined': ['illdefined', 'ill defined', 'ill', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'indistinct_margins': ['indistinct', 'indistinct margins'],
                              'oblong': 'oblong',
                              'invasive': 'invasive',
                              'NA': ['na', 'mammography not done for diagnosis', 'nan'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
                              }

    elif db_column_name == 'tomography_y_n':
        col_values_dict = {'yes': 'yes',
                           'no': 'no',
                           'NA': ['na', 'mammography not done for diagnosis'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'automated_breast_volume_scanner_abvs':
        col_values_dict = {'yes': 'automated breast volume scanner done',
                           'no': 'automated breast volume scanner not done',
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'sonomammography_status':
        col_values_dict = {'yes': 'sono-mammography done',
                           'no': 'sonomammography not done for diagnosis',
                           'NA': ['na', 'nan'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'sonomammo_breast':
        col_values_dict = {'bilateral': 'bilateral',
                           'right_breast': ['right breast', 'right'],
                           'left_breast': ['left breast', 'left'],
                           'left_axilla': 'left axilla',
                           'right_axilla': 'right axilla',
                           'NA': ['na', 'sonomammography not done for diagnosis', 'nan'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                        'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                        'data not in report']
                            }

    elif db_column_name == 'sonomammo_mass':
        col_values_dict = {'yes': 'mass/lesion detected',
                           'no': 'no mass detected',
                           'NA': ['na', 'sonomammography not done for diagnosis', 'nan'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'sonomammo_mass_shape':
        col_values_dict = {'irregular': 'irregular',
                              'oval': ['oval', 'small ovoid'],
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'well_marginated': 'well marginated',
                              'lobulated': ['lobulated', 'lobulations'],
                              'microlobulated': ['microlobulated', 'macro-lobulated'],
                              'ill_defined': ['illdefined', 'ill defined', 'ill', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'indistinct_margins': ['indistinct', 'indistinct margins'],
                              'oblong': 'oblong',
                              'invasive': 'invasive',
                              'NA': ['na', 'sonomammography not done for diagnosis', 'nan'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
                              }

    elif db_column_name == 'sonomammo_mass_margin':
        col_values_dict = {'irregular': 'irregular',
                              'oval': ['oval', 'small ovoid'],
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'well_marginated': 'well marginated',
                              'lobulated': ['lobulated', 'lobulations'],
                              'microlobulated': ['microlobulated', 'macro-lobulated', 'macrolobulated'],
                              'ill_defined': ['illdefined', 'ill defined', 'ill', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'indistinct_margins': ['indistinct', 'indistinct margins'],
                              'oblong': 'oblong',
                              'invasive': 'invasive',
                              'NA': ['na', 'sonomammography not done for diagnosis', 'nan'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
                              }

    elif db_column_name == 'mri_status':
        col_values_dict = {'yes': 'mri-breast done',
                           'no': 'mri-breast not done',
                           'NA': ['na', 'nan'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'mri_breast':
        col_values_dict = {'left_breast': 'left breast',
                           'right_breast': 'right breast',
                           'bilateral': 'bilateral',
                           'NA': ['mri-breast not done', 'nan'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'background_paranchymal_enhancement_level_mri':
        col_values_dict = {'mild': 'mild',
                           'marked': 'marked',
                           'minimal': 'minimal',
                           'moderate': 'moderate',
                           'NA': ['na', 'mri-breast not done', 'nan'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'background_paranchymal_enhancement_symmetry_mri':
        col_values_dict = {'symmetric': 'symmetric',
                           'NA': ['na', 'mri-breast not done', 'nan'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'mass_mri':
        col_values_dict = {'yes': 'mass detected',
                           'no': 'no mass detected',
                           'NA': ['na', 'mri-breast not done', 'nan'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }
    elif db_column_name == 'mass_location_mri':
        col_values_dict = {'left_breast': 'left breast',
                           'right_breast': 'right breast',
                           'bilateral': 'bilateral',
                           'NA': ['na', 'nan', 'mri-breast not done'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'mass_shape_mri':
        col_values_dict = {'irregular': 'irregular',
                              'oval': ['oval', 'small ovoid'],
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'well_marginated': 'well marginated',
                              'lobulated': ['lobulated', 'lobulations'],
                              'microlobulated': ['microlobulated', 'macro-lobulated'],
                              'ill_defined': ['illdefined', 'ill defined', 'ill', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'indistinct_margins': ['indistinct', 'indistinct margins'],
                              'oblong': 'oblong',
                              'invasive': 'invasive',
                              'NA': ['na', 'mri-breast not done', 'nan'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
                              }

    elif db_column_name == 'mass_margin_mri':
        col_values_dict = {'irregular': 'irregular',
                              'oval': ['oval', 'small ovoid'],
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'well_marginated': 'well marginated',
                              'lobulated': ['lobulated', 'lobulations'],
                              'microlobulated': ['microlobulated', 'macro-lobulated'],
                              'ill_defined': ['illdefined', 'ill defined', 'ill', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'indistinct_margins': ['indistinct', 'indistinct margins'],
                              'oblong': 'oblong',
                              'invasive': 'invasive',
                              'NA': ['na', 'mri-breast not done', 'nan'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
                              }

    elif db_column_name == 'pet_carcinoma_status':
        col_values_dict = {'pre_operative': 'pre-operative',
                             'post_operative': 'post-operative',
                             'NA': ['na', 'pet_report_not_present'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                    'requires follow up'],
                             'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report', 'data_not_availabel']
                             }

    elif db_column_name == 'pet_cancer_location':
        col_values_dict = {'right_breast': 'right_breast',
                            'left_breast': 'left_breast',
                            'bilateral': 'bilateral',
                            'right_axillary_lymph_node': 'Right axillary lymph node',
                            'thorax': 'thorax',
                            'NA': ['na', 'pet_report_not_present'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                    'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report', 'data_not_availabel']
                            }

    elif db_column_name == 'pet_procedure_body_region':
        col_values_dict = {'skull_to_mid_thigh': ['skull_to_mid_thigh', 'skull to mid thigh'],
                           'skull_to_upper_thigh': 'Vertex to upper thigh (Skull to upper thigh)',
                           'abdomen and pelvis': ['abdomen and pelvis', 'scan of abdomen and pelvis', 'whole abdomen and pelvis',
                                                  'chest abdomen and pelvis', 'ct of abdomen pelvis'],
                           'ct_thorax': ['thorax', 'ct scan of thorax', 'ct thorax', 'CT Scan Thorax'],
                           'hrct_thorax': ['hrct of thorax', 'hrct thorax'],
                           'ct_brain': 'ct brain with and without contrast',
                           'abdomen': ['abdomen', 'ct scan abdomen', 'abdomen ct (plain and with oral and IV contrast)'],
                           'pelvis': 'pelvis',
                           'liver': 'liver',
                           'ct_scan_of_pulmonary_angiography': ['CT scan of pulmonary Angiography', 'ct mesentric angiography'],
                           'skeletal_system': 'skeletal system',
                           'left_breast': ['left breast', 'left_breast'],
                           'right_breast': ['right_breast', 'right breast'],
                           'whole_body': ['whole body', 'whole body pet ct scan ', 'Whole body bone scan report',
                                          'whole body scan'],
                           'cect_chest': 'cect_chest',
                           'bone_scan': ['bone scan', 'whole body bone scan', 'whole body bone scan report'],
                           'ct_scan_of_chest': ['ct scan of chest', 'c.t of the chest', 'ct chest', 'chest', 'chest ',
                                                'chest (plain and constrast)', 'ct chest and abdomen (p+c)',
                                                'chest ct scan'],
                           'NA': ['na', 'pet_report_not_present', 'nan'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel']
                            }

    elif db_column_name == 'pet_primary_disease_yes_no':
        col_values_dict = {'yes': 'primary_disease',
                                   'no': ['no_primary_disease', 'not_primary_disease'],
                                    'NA': ['na', 'pet_report_not_present'],
                                    'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                    'requires follow up'],
                                    'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report', 'data_not_availabel']
                                   }

    elif db_column_name == 'pet_local_spread':
        col_values_dict = {'yes': 'local_spread_present',
                           'no': 'no_local_spread',
                           'NA': ['na', 'pet_report_not_present'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel']
                           }

    elif db_column_name == 'pet_recurrence_yes_no':
        col_values_dict = {'yes': ['recurrence_present', 'yes_recurrence_present'],
                              'no': ['no_recurrence_present', 'no_recurrence'],
                              'NA': ['na', 'pet_report_not_present'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                     'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                     'data not in report', 'data_not_availabel']
                              }

    elif db_column_name == 'pet_distant_metastasis':
        col_values_dict = {'yes': ['metastasis', 'possible_metastasis', 'distant_metastasis_present'],
                               'no': 'no_metastasis',
                               'NA': ['na', 'pet_report_not_present'],
                               'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                        'requires follow up'],
                               'data_not_available': ['data not available', 'data_not_available',
                                                        'data not in report', 'data_not_availabel']
                               }

    elif db_column_name == 'nact_status':
        col_values_dict = {'yes': ['yes', 'nact_given', 'nact given', 'nact_and_naht_given'],
                    'no': ['no', 'nact not given', 'nact/naht not given', 'naht_given'],
                    'NA': 'na',
                    'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                    'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                    'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                    }

    elif db_column_name == 'place_nact':
        col_values_dict = {'pccm': 'at pccm',
                   'outside': 'outside',
                   'NA': ['na', 'nact not given', 'nact/naht not given'],
                   'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                   'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                   'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                   }

    # elif db_column_name == 'details_nact':
    #     col_values_dict = {'details_available': ['details available', 'ac 4 cycles followed by weekly paclitaxel 12 weeks',
    #                                         '4 cycles of EC + docetaxel', '4 cycles of ec '],
    #                  'NA': ['na', 'nact not given', 'nact/naht not given'],
    #                  'requires_follow_up': ['requires_follow_up', 'requires follow-up',
    #                                     'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
    #                 'data_not_available': ['data not available', 'data_not_available',
    #                                             'data not in report', 'data_not_availabel'],
    #                 'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
    #                }

    elif db_column_name == 'toxicity_type':
        col_values_dict = {'no_toxicity': ['no toxicity', 'no'],
                           'neuropathy': 'neuropathy',
                           'vomiting': 'vomiting',
                           'pain_and_increasing_size': 'pain and increasing size',
                           'neutropenia': ['neutropenia', 'severe neutropenia'],
                           'nausea': 'nausea',
                           'joint_pain': 'joint pain',
                           'cardiotoxicity': 'cardiotoxicity',
                           'weakness': 'weakness',
                           'fever': 'fever',
                           'breathlessness': 'breathlessness',
                           'thrombocytopenia': 'thrombocytopenia',
                           'NA': ['na', 'nact not given', 'nact/naht not given', 'adjuvant chemotherapy not given'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required']
                           }

    elif db_column_name == 'toxicity_grade':
        col_values_dict = {'mild': 'mild',
                           'moderate': 'moderate',
                           'severe': 'severe',
                           'NA': ['na', 'nact not given', 'nact/naht not given', 'no toxicity',
                                  'adjuvant chemotherapy not given'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required']
                           }

    elif db_column_name == 'toxicity_response':
        col_values_dict = {'complete': 'complete',
                            'partial': 'partial',
                            'NA': ['na', 'no toxicity', 'no', 'nact not given', 'nact/naht not given',
                                   'adjuvant chemotherapy not given', 'no treatment given'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                            'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                            'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                            }

    elif db_column_name == 'tumour_response_check_method':
        col_values_dict = {'sonomammography': ['sonomammography' 'sono mammography', 'sonomammography'],
                           'mammography': ['mammography', 'mammography '],
                           'ultrasound': ['left breast ultrasound', 'usg', 'ultrasound'],
                           'mri': 'mri',
                           'pet_ct' : ['pet ct'],
                           'NA': ['na', 'nact not given', 'nact/naht not given'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                        'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'tumour_response_nact':
        col_values_dict = {'complete': 'complete',
                           'partial': 'partial',
                           'progression': 'progression',
                           'progressive': ['progressive', 'progressing'],
                           'no_effect': 'no effect',
                           'NA': ['na', 'nact not given', 'nact/naht not given'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'nact_completion_status':
        col_values_dict = {'complete': ['nact_complete', 'nact completed as per schedule'],
                           'incomplete': ['incomplete', 'nact incomplete'],
                           'NA': ['na', 'nact not given', 'nact/naht not given'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'trastuzumab_use_nact':
        col_values_dict = {'yes': 'trastuzumab used',
                             'no': ['trastuzumab not used', 'no_neo_adjuvant_trastuzumab'],
                             'NA': ['na', 'nact not given', 'nact/naht not given'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                             'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                             'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                             }

    elif db_column_name == 'hormone_therapy_nact':
        col_values_dict = {'yes': ['yes', 'naht_given', 'naht given', 'hormone therapy given', 'hormone therapy nact given',
                                     'hormone therapy recieved', 'naht_yes'],
                             'no': ['no_naht', 'nact/naht not given', 'no hormone therapy given',
                                    'naht_not given', 'naht_not given'],
                             'NA': ['na', 'nact not given'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                             'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                             'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                             }

    elif db_column_name == 'radiation_received':
        col_values_dict = {'yes': ['radiation therapy recieved', 'radiation therapy recieved',
                                   'radiation therapy received', 'radiotherapy given but data not available'],
                           'requires_follow_up': ['not indicated', 'requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel', 'data not in report '],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'imrt_dcrt':
        col_values_dict = {'yes': ['imrt/3dcrt_yes',
                           'patient opted for intensity modulated/3dimensional conformal radiotherapy (imrt/3dcrt)'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                         'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'NA': 'na',
                           'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                            }

    elif db_column_name == 'radiation_ipsilateral_breast':
        col_values_dict = {'right_breast': 'rt_given',
                           'left_breast': ['left breast', 'left_breast', 'lt_given'],
                                'NA': ['na', 'not_given'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                            }

    elif db_column_name == 'radiation_chest_wall':
        col_values_dict = {'right_breast': 'rt_given',
                           'left_breast': ['left breast', 'left_breast', 'lt_given'],
                                'NA': ['na', 'not_given'],
                                'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                                'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                                'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                                     }

    elif db_column_name == 'radiation_supraclavicular_fossa':
        col_values_dict = {'right_breast': 'rt_given',
                           'left_breast': ['left breast', 'left_breast', 'lt_given'],
                           'NA': ['na', 'not_given'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'radiation_axilla':
        col_values_dict = {'right_breast': 'rt_given',
                           'left_breast': ['left breast', 'left_breast', 'lt_given'],
                           'NA': ['na', 'not_given'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'radiation_ipsilateral_breast_boost':
        col_values_dict = {'right_breast_boost': 'rt_boost_given',
                           'left_breast_boost_given': 'lt_boost_given',
                           'NA': ['na', 'not_given', 'boost_not_given'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'radiation_delayed_toxicity':
        col_values_dict = {'yes': 'grade 1 skin reaction',
                            'no': 'no',
                            'NA': 'na',
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                            'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel', 'not known'],
                            'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                            }

    elif db_column_name == 'radiation_location':
        col_values_dict = {'left_breast': ['left_breast', 'left breast'],
                           'right_breast': ['right_breast', 'right_breat', 'right whole breast'],
                           'bilateral_breast': ['b/l breast', 'bilateral', 'bilateral breast'],
                           'left_scf': ['left scf', 'left_scf'],
                           'right_scf': ['right scf', 'right_scf'],
                           'right_axilla': ['right_axilla', 'right axilla'],
                           'left_axilla': ['left_axilla', 'left axillas'],
                           'left_breast_chest_wall': ['left breast chest wall', 'left_breast_chest_wall', 'left chest wall'],
                           'right_breast_chest_wall': ['right breast chest wall', 'right_breast_chest_wall'],
                           'tumour_bed': ['tumour_bed', 'tumour bed', 'tumour'],
                           'supraclavicular_area': ['supraclavicular area', 'supraclavicular'],
                           'right_supraclavicular_region': ['right supraclavicular region', 'right_supraclavicular_region'],
                           'left_supraclavicular_region': ['left supraclavicular region', 'left_supraclavicular_region'],
                           'sib': 'sib',
                           'scf': 'scf',
                           'electron_boost': 'electron boost',
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'hormone_indicated':
        col_values_dict = {'yes': 'hormone therapy indicated',
                          'no': 'hormone therapy not indicated',
                          'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires followup',
                                                 'requires follow up', 'not certain, requires follow-up',
                                                 'follow-up required'],
                          'data_not_available': ['data not available', 'data_not_available',
                                                 'data not in report', 'data_not_availabel'],
                          'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                          }

    elif db_column_name == 'hormone_recieved':
        col_values_dict = {'yes': 'hormone therapy recieved',
                            'no': 'no hormone therapy recieved',
                            'NA': 'na',
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires followup',
                                'requires follow up', 'not certain, requires follow-up',
                                'follow-up required'],
                            'data_not_available': ['data not available', 'data_not_available',
                                'data not in report', 'data_not_availabel'],
                            'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                            }

    elif  db_column_name == 'hormone_discontinued':
        col_values_dict = {'yes': ['stopped by patient', 'yes', 'completion of planned course'],
                             'no': ['therapy is ongoing', 'thearpy is ongoing', 'ongoing'],
                             'NA': 'na',
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires followup',
                                                 'requires follow up', 'not certain, requires follow-up',
                                                 'follow-up required'],
                             'data_not_available': ['data not available', 'data_not_available',
                                                 'data not in report', 'data_not_availabel'],
                             'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                             }

    elif db_column_name == 'hormone_therapy_outcome':
        col_values_dict = {'good': 'good',
                           'therapy_is_ongoing': ['therapy ongoing', 'therapy is ongoing', 'ongoing', 'ongong', 'exemestane- ongoing'],
                           'complete': 'completed',
                           'discontinued': ['discontinued', ' stopped by patient'],
                           'NA': 'na',
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires followup',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required', 'required follow-up', 'requires folow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'hormone_followup':
        col_values_dict = {'therapy_is_ongoing': ['therapy ongoing', 'therapy is ongoing', 'ongoing', 'continued'],
                         'complete': 'completed',
                         'discontinued': ['discontinued', ' stopped by patient'],
                         'NA': 'na',
                         'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up',
                                                'follow-up required', 'required follow-up'],
                         'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                         'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                         }

    elif db_column_name == 'horomone_recurrence':
        col_values_dict = {'yes': 'recurrence',
                           'no': 'no recurrence',
                           'NA': 'na',
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                            'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                            'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'metastasis_exam':
        col_values_dict = {'yes': 'examined for metastatic disease',
                        'no': ['not examined for metastatic disease', 'no examined for metastatic disease'],
                        'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                        'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                        'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                        }

    elif db_column_name == 'nature_of_recurrence':
        col_values_dict = {'local': ['local', 'local (right axillary nodal metastasis)'],
                             'distant': 'distant',
                             'metastasis': 'metastasis',
                             'NA': ['na', 'no recurrence'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                             'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                             'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                             }

    elif db_column_name == 'distant_site':
        col_values_dict = {'right_breast': ['right_breast', 'right breast', 'right breast '],
                           'left_breast': ['left_breast', 'left breast'],
                           'right_axilla': ['right_axilla', 'right axilla'],
                           'left_axilla': ['left_axilla', 'left axilla'],
                           'liver': 'liver',
                           'brain_metastasis': 'brain metastasis',
                           'left_side_neck': 'left side neck',
                           'right_side_neck': 'right side neck',
                           'left_axillary_node': 'left axillary node',
                           'right_axillary_node': 'right axillary node',
                           'pancreas': 'pancreas',
                           'left_chest_wall': 'left chest wall',
                           'right_chest_wall': 'right chest wall',
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'patient_status_last_followup':
        col_values_dict = {'survivor': 'survivor',
                           'deceased:due_to_disease': ['deceased: due to disease', 'deceased, due to disease'],
                           'deceased:due_to_unrelated_causes': ['deceased: requires specialist input',
                                                                'deceased', 'deceased: data not in report',
                                                                'deceased, due to unrelated causes',
                                                                'deceased: due to unrelated causes'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    elif db_column_name == 'chemotherapy_status':
        col_values_dict = {'yes': ['act_given', 'adjuvant chemotherapy given'],
                            'no': 'adjuvant chemotherapy not given',
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                   'requires follow up', 'not certain, requires follow-up',
                                                   'follow-up required'],
                            'data_not_available': ['data not available', 'data_not_available',
                                                   'data not in report', 'data_not_availabel'],
                            'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                            }

    elif db_column_name == 'place_chemotherapy':
        col_values_dict = {'pccm': 'at pccm',
                   'outside': 'outside',
                   'NA': ['na', 'adjuvant chemotherapy not given'],
                   'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                   'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                   'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                   }

    elif db_column_name == 'details_chemotherapy':
        col_values_dict = {'details_available': ['details available', '6 cycle herceptin',
                                            'ec folowed by paclitaxel + herceptin '],
                     'NA': ['na', 'adjuvant chemotherapy not given'],
                     'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                    'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                    'lost_to_follow_up': [' lost to follow up', 'lost to follow-up']
                   }

    elif db_column_name == 'chemotherapy_completion_status':
        col_values_dict = {'complete': ['nact_complete', 'nact completed as per schedule',
                                        'adjuvant chemotherapy completed as per schedule'],
                           'incomplete': ['incomplete', 'nact incomplete'],
                           'NA': ['na', 'nact not given', 'nact/naht not given', 'adjuvant chemotherapy not given'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow-up']
                           }

    elif db_column_name == 'trastuzumab_use_chemotherapy':
        col_values_dict = {'yes': ['trastuzumab used', 'yes'],
                                'no': 'trastuzumab not used',
                                'NA': ['na', 'adjuvant chemotherapy not given'],
                                'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                                'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                                'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                                }

    elif db_column_name == 'ovary_status':
        col_values_dict = {'pre_menopausal': ['pre-menopausal', 'premenopausal', 'premanopausal', 'menses ongoing',
                                        ' pre-menopausal', 'amenorrhea on chemotherapy;regular menses after chemo'],
                         'post_menopausal': ['post-menopausal', 'post-menopause', 'post menopausal', 'postmenopausal'],
                         'peri_menopausal': 'peri-menopausal',
                         'hysterectomy': ['hysterectomy', 'hysterctomy', 'post hysterectomy', 'hysterectome',
                                         'post -menopausal(hysterectomy done in 2012)', 'hysteroctomy',
                                          'post menopausal (hysterectomy)'],
                        'oopherectomy': ['oophorectomy', 'bilateral oopherectomy'],
                        'other': 'male',
                        'NA': ['na', 'adjuvant chemotherapy not given'],
                        'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up',
                                               'follow-up required'],
                        'data_not_available': ['data not available', 'data_not_available', 'data not in report'],
                        'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                        }

    elif db_column_name == 'hormone_therapy_chemotherapy':
        col_values_dict = {'yes': 'hormone therapy given',
                                     'no': 'no hormone therapy given',
                                     'NA': ['na', 'adjuvant chemotherapy not given'],
                                     'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                            'requires follow up', 'follow-up required'],
                                     'data_not_available': ['data not available', 'data_not_available', 'data not in report'],
                                     'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                                     }

    elif db_column_name == 'patient_status_last_followup':
        col_values_dict = {'survivor': 'survivor',
                           'deceased:due_to_disease': ['deceased: due to disease', 'deceased, due to disease'],
                           'deceased:due_to_unrelated_causes': ['deceased: requires specialist input', 'deceased',
                                                                'deceased: data not in report',
                                                                'deceased, due to unrelated causes',
                                                                'deceased: due to unrelated causes',
                                                                'deceased: not known'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                            'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    return col_values_dict


##

def curation_cols(table_name):
    cols_to_be_curated = 'NA'
    if table_name == 'patient_information_history':
        cols_to_be_curated = {'type_physical_activity': 'physical_activity_dict',
                 'diet': 'diet_dict',
                 'marital_status': 'marital_status_dict',
                 'menopause_status': 'menopause_status_dict',
                 # 'age_at_menopause_yrs': 'age_at_menopause_yrs_dict',
                 'current_breast_cancer_detected_by': 'current_breast_cancer_detected_by_dict',
                 'lb_symptoms': 'rb_lb_symptoms_dict',
                 'rb_symptoms': 'rb_lb_symptoms_dict',
                 'success_fertility_treatment': 'success_fertility_treatment_dict',
                 'patient_metastasis_symptoms': 'patient_metastasis_symptoms_dict'}

    elif table_name == 'radiology':
        cols_to_be_curated = {'mammography': 'mammography_dict',
                                'mammography_breast': 'mammography_breast_dict',
                                'mammography_massshape': 'mammography_massshape_dict',
                                'mammography_massmargin': 'mammography_massshape_dict',
                                'tomography_y_n': 'tomography_y_n_dict',
                                'automated_breast_volume_scanner_abvs': 'automated_breast_volume_scanner_abvs_dict',
                                'sonomammography_status': 'sonomammography_status_dict',
                                'sonomammo_breast': 'sonomammo_breast_dict',
                                'sonomammo_mass': 'sonomammo_mass_dict',
                                'sonomammo_mass_shape': 'mammography_massshape_dict',
                                'sonomammo_mass_margin': 'mammography_massshape_dict',
                                'mri_status': 'mri_status_dict',
                                'mri_breast': 'mri_breast_dict',
                                'background_paranchymal_enhancement_level_mri': 'background_paranchymal_enhancement_level_mri_dict',
                                'background_paranchymal_enhancement_symmetry_mri': 'background_paranchymal_enhancement_symmetry_mri_dict',
                                'mass_mri': 'mass_mri_dict',
                                'mass_location_mri': 'mass_location_mri_dict',
                                'mass_shape_mri': 'mass_shape_mri_dict',
                                'mass_margin_mri': 'mass_margin_mri_dict'
                                }

    elif table_name == 'pet_reports':
        cols_to_be_curated = {'pet_carcinoma_status': 'pet_carcinoma_status_dict',
                             'pet_cancer_location': 'pet_cancer_location_dict',
                             'pet_procedure_body_region': 'pet_procedure_body_region_dict',
                             'pet_primary_disease_yes_no': 'pet_primary_disease_yes_no_dict',
                             'pet_local_spread': 'pet_local_spread_dict',
                             'pet_recurrence_yes_no': 'pet_recurrence_yes_no_dict',
                             'pet_distant_metastasis': 'pet_distant_metastasis_dict'
                             }

    elif table_name == 'neo_adjuvant_therapy':
        cols_to_be_curated = {'nact_status': 'nact_status_dict',
                                      'place_nact': 'place_nact_dict',
                                      # 'details_nact': 'details_nact_dict',
                                      'toxicity_type': 'toxicity_type_dict',
                                      'toxicity_grade': 'toxicity_grade_dict',
                                      'toxicity_response': 'toxicity_response_dict',
                                      'tumour_response_check_method': 'tumour_response_check_method_dict',
                                      'tumour_response_nact': 'tumour_response_nact_dict',
                                      'nact_completion_status': 'nact_completion_status_dict',
                                      'trastuzumab_use_nact': 'trastuzumab_use_nact_dict',
                                      'hormone_therapy_nact': 'hormone_therapy_nact_dict'}

    elif table_name == 'radiotherapy':
        cols_to_be_curated = {'radiation_received': 'radiation_received_dict',
                              'imrt_dcrt': 'imrt_dcrt_dict',
                              'radiation_ipsilateral_breast': 'radiation_ipsilateral_breast_dict',
                              'radiation_chest_wall': 'radiation_chest_wall_dict',
                              'radiation_supraclavicular_fossa': 'radiation_supraclavicular_fossa_dict',
                              'radiation_axilla': 'radiation_axilla_dict',
                              'radiation_ipsilateral_breast_boost': 'radiation_ipsilateral_breast_boost_dict',
                              'radiation_delayed_toxicity': 'radiation_delayed_toxicity_dict'}

    elif table_name == 'hormonetherapy_survival':
        cols_to_be_curated = {'hormone_indicated': 'hormone_indicated_dict',
                                         'hormone_recieved': 'hormone_recieved_dict',
                                         'hormone_discontinued': 'hormone_discontinued_dict',
                                         'hormone_therapy_outcome': 'hormone_therapy_outcome_dict',
                                         'hormone_followup': 'hormone_followup_dict',
                                         'horomone_recurrence': 'hormone_recurrence_dict',
                                         'metastasis_exam': 'metastasis_exam_dict',
                                         'nature_of_recurrence': 'nature_of_recurrence_dict'
                                         }

    elif table_name == 'adjuvant_chemotherapy':
        cols_to_be_curated = {'chemotherapy_status': 'adjuvant_chemotherapy_status_dict',
                                       'place_chemotherapy': 'place_chemotherapy_dict',
                                       'details_chemotherapy': 'details_chemotherapy_dict',
                                       'toxicity_type': 'toxicity_type_dict',
                                       'toxicity_grade': 'toxicity_grade_dict',
                                       'toxicity_response': 'toxicity_response_dict',
                                       'chemotherapy_completion_status': 'chemotherapy_completion_status_dict',
                                       'trastuzumab_use_chemotherapy': 'trastuzumab_use_chemotherapy_dict',
                                       'ovary_status': 'ovary_status_dict',
                                       'hormone_therapy_chemotherapy': 'hormone_therapy_chemotherapy_dict'
                                       }

    elif table_name == 'follow_up_data':
        cols_to_be_curated = {'follow_up_status': 'follow_up_status_dict'}

    return cols_to_be_curated

