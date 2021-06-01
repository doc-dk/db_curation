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
                             'lower_intensity_exercise': ['lower intensity exercise'],
                             'aerobic_exercise': ['aerobic exercise', 'other aerobic exercise'],
                             'yoga': 'yoga',
                             'playing': ['badminton', 'tennis', 'throw ball', 'ball'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                             'no_physical_activities': ['no_physical_activities', 'no physical activities'],
                             'data_not_available': ['data not available', 'data_not_available']
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
        col_values_dict = {'married': ['married', 'maried'],
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
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                           }

    elif db_column_name == 'current_breast_cancer_detected_by':
        col_values_dict = {'self': 'self',
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
        col_values_dict = {'lumps': ['lumps', 'lump'],
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
        col_values_dict = {'lumps': ['lumps', 'lump'],
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
        col_values_dict = {'weight_loss': 'weight loss',
                                    'cough': 'cough',
                                    'bone_pain': 'bone pain',
                                    'headache':'headache',
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
                              'oval': 'oval',
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'lobulated': 'lobulated',
                              'ill_defined': ['illdefined', 'ill defined', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'NA': ['na', 'mammography not done for diagnosis'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
                              }

    elif db_column_name == 'mammography_massmargin':
        col_values_dict = {'irregular': 'irregular',
                              'oval': 'oval',
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'lobulated': 'lobulated',
                              'ill_defined': ['illdefined', 'ill defined', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'NA': ['na', 'mammography not done for diagnosis'],
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
                            'NA': ['na', 'mammography not done for diagnosis'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                        'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available',
                                                        'data not in report']
                            }

    elif db_column_name == 'sonomammo_mass':
        col_values_dict = {'yes': 'mass/lesion detected',
                           'no': 'no mass detected',
                           'NA': ['na', 'sonomammography not done for diagnosis'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'sonomammo_mass_shape':
        col_values_dict = {'irregular': 'irregular',
                              'oval': 'oval',
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'lobulated': 'lobulated',
                              'ill_defined': ['illdefined', 'ill defined', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'NA': ['na', 'mammography not done for diagnosis'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
                              }
    elif db_column_name == 'sonomammo_mass_margin':
        col_values_dict = {'irregular': 'irregular',
                              'oval': 'oval',
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'lobulated': 'lobulated',
                              'ill_defined': ['illdefined', 'ill defined', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'NA': ['na', 'mammography not done for diagnosis'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
                              }

    elif db_column_name == 'mri_status':
        col_values_dict = {'yes': 'mri-breast done',
                           'no': 'mri-breast not done',
                           'NA': 'na',
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }
    elif db_column_name == 'mri_breast':
        col_values_dict = {'left_breast': 'left breast',
                           'right_breast': 'right breast',
                           'bilateral': 'bilateral',
                           'NA': 'mri-breast not done',
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
                           'NA': 'mri-breast not done',
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'background_paranchymal_enhancement_symmetry_mri':
        col_values_dict = {'symmetric': 'symmetric',
                           'NA': ['na', 'mri-breast not done'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }

    elif db_column_name == 'mass_mri':
        col_values_dict = {'yes': 'mass detected',
                           'no': 'no mass detected',
                           'NA': ['na', 'mri-breast not done'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report']
                           }
    elif db_column_name == 'mass_location_mri':
        col_values_dict = {'left_breast': 'left breast',
                           'right_breast': 'right breast',
                           'bilateral': 'bilateral',
                           'NA': 'mri-breast not done',
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
    elif db_column_name == 'mass_shape_mri':
        col_values_dict = {'irregular': 'irregular',
                              'oval': 'oval',
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'lobulated': 'lobulated',
                              'ill_defined': ['illdefined', 'ill defined', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'NA': ['na', 'mammography not done for diagnosis'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
                              }
    elif db_column_name == 'mass_margin_mri':
        col_values_dict = {'irregular': 'irregular',
                              'oval': 'oval',
                              'round': ['round', 'rouded'],
                              'spiculated': ['spiculated', 'spiculations'],
                              'well_defined': ['well defined', 'well-defined'],
                              'lobulated': 'lobulated',
                              'ill_defined': ['illdefined', 'ill defined', 'ill defined posterior margin'],
                              'circumscribed': ['circumscribed', 'partially circumscribed'],
                              'obscured': ['obscured', 'partially obscured'],
                              'radiopaque': ['radio opaque', 'radioopaque', 'radiopaque'],
                              'asymmetric': 'asymmetric',
                              'abnormal': 'abnormal',
                              'angular': 'angular',
                              'posterior': 'posterior',
                              'NA': ['na', 'mammography not done for diagnosis'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
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
    elif db_column_name == 'pet_primary_disease_yes_no':
        col_values_dict = {'yes': 'primary_disease',
                                   'no': ['no_primary_disease', 'not_primary_disease'],
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
        col_values_dict = {'distant_metastasis': ['metastasis', 'possible_metastasis', 'distant_metastasis_present'],
                               'no_distant_metastasis': 'no_metastasis',
                               'NA': ['na', 'pet_report_not_present'],
                               'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                        'requires follow up'],
                               'data_not_available': ['data not available', 'data_not_available',
                                                        'data not in report', 'data_not_availabel']
                               }
    elif db_column_name == 'nact_status':
        col_values_dict = {'yes': ['yes', 'nact_given', 'NACT given', 'nact_and_naht_given'],
                    'no': ['no', 'nact not given', 'nact/naht not given', 'nact_and_naht_given'],
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
    elif db_column_name == 'details_nact':
        col_values_dict = {'details_available': ['details available', 'ac 4 cycles followed by weekly paclitaxel 12 weeks',
                                            '4 cycles of EC + docetaxel', '4 cycles of ec '],
                     'NA': ['na', 'nact not given', 'nact/naht not given'],
                     'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                    'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                    'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                   }
    elif db_column_name == 'toxicity_response':
        col_values_dict = {'complete': 'complete',
                            'partial': 'partial',
                            'NA': ['na', 'no toxicity', 'nact not given', 'nact/naht not given'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
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
        col_values_dict = {'yes': ['yes', 'naht_given', 'hormone therapy given', 'hormone therapy nact given',
                                     'hormone therapy recieved', 'naht_yes'],
                             'no': ['no_naht', 'nact/naht not given', 'no hormone therapy given',
                                    'naht_not given', 'naht_not given'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                             'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                             'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                             }
    elif db_column_name == 'radiation_received':
        col_values_dict = {'yes': ['radiation therapy recieved', 'radiation therapy recieved'],
                           'requires_follow_up': ['not indicated', 'requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }
    elif db_column_name == 'imrt_dcrt':
        col_values_dict = {'yes': ['imrt/3dcrt_yes',
                          'patient opted for intensity modulated/3dimensional conformal radiotherapy (imrt/3dcrt)'],
                  'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                         'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                  'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                  'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                  }
    elif db_column_name == 'radiation_ipsilateral_breast':
        col_values_dict = {'right_breast': 'rt_given',
                                     'NA': ['na', 'not_given'],
                                     'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                                     'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                                     'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                                     }
    elif db_column_name == 'radiation_delayed_toxicity':
        col_values_dict = {'yes': 'grade 1 skin reaction',
                                   'no': 'no',
                                    'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
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
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires followup',
                                'requires follow up', 'not certain, requires follow-up',
                                'follow-up required'],
                            'data_not_available': ['data not available', 'data_not_available',
                                'data not in report', 'data_not_availabel'],
                            'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                            }
    elif db_column_name == 'hormone_discontinued':
        col_values_dict = {'yes': ['stopped by patient', 'yes', 'completion of planned course'],
                             'no': ['therapy is ongoing', 'thearpy is ongoing', 'ongoing'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires followup',
                                                 'requires follow up', 'not certain, requires follow-up',
                                                 'follow-up required'],
                             'data_not_available': ['data not available', 'data_not_available',
                                                 'data not in report', 'data_not_availabel'],
                             'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                             }
    elif db_column_name == 'hormone_followup':
        col_values_dict = {'therapy_is_ongoing': ['therapy ongoing', 'therapy is ongoing', 'ongoing', 'continued'],
                         'complete': 'completed',
                         'discontinued': ['discontinued', ' stopped by patient'],
                         'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                         'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                         'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                         }
    elif db_column_name == 'horomone_recurrence':
        col_values_dict = {'yes': 'recurrence',
                           'no': 'no recurrence',
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
                             'distant_and_local': 'distant and local',
                             'NA': ['na', 'no recurrence'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
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

    elif db_column_name == 'trastuzumab_use_chemotherapy':
        col_values_dict = {'yes': 'trastuzumab used',
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
                                         'post -menopausal(hysterectomy done in 2012)', 'post menopausal (hysterectomy)'],
                        'oopherectomy': ['oophorectomy', 'bilateral oopherectomy'],
                        'other': 'male',
                        'NA': ['na', 'adjuvant chemotherapy not given'],
                        'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
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
                             'pet_primary_disease_yes_no': 'pet_primary_disease_yes_no_dict',
                             'pet_recurrence_yes_no': 'pet_recurrence_yes_no_dict',
                             'pet_distant_metastasis': 'pet_distant_metastasis_dict'
                             }
    elif table_name == 'neo_adjuvant_therapy':
        cols_to_be_curated = {'nact_status': 'nact_status_dict',
                                      'place_nact': 'place_nact_dict',
                                      'details_nact': 'details_nact_dict',
                                      'toxicity_response': 'toxicity_response_dict',
                                      'trastuzumab_use_nact': 'trastuzumab_use_nact_dict',
                                      'hormone_therapy_nact': 'hormone_therapy_nact_dict'}
    elif table_name == 'radiotherapy':
        cols_to_be_curated = {'radiation_received': 'radiation_received_dict',
                              'imrt_dcrt': 'imrt_dcrt_dict',
                              'radiation_ipsilateral_breast': 'radiation_ipsilateral_breast_dict',
                              'radiation_delayed_toxicity': 'radiation_delayed_toxicity_dict'}

    elif table_name == 'hormonetherapy_survival':
        cols_to_be_curated = {'hormone_indicated': 'hormone_indicated_dict',
                                         'hormone_recieved': 'hormone_recieved_dict',
                                         'hormone_discontinued': 'hormone_discontinued_dict',
                                         'hormone_followup': 'hormone_followup_dict',
                                         'horomone_recurrence': 'hormone_recurrence_dict',
                                         'metastasis_exam': 'metastasis_exam_dict',
                                         'nature_of_recurrence': 'nature_of_recurrence_dict'
                                         }
    elif table_name == 'adjuvant_chemotherapy':
        cols_to_be_curated = {'chemotherapy_status': 'adjuvant_chemotherapy_status_dict',
                                       'place_chemotherapy': 'place_chemotherapy_dict',
                                       'details_chemotherapy': 'details_chemotherapy_dict',
                                       'trastuzumab_use_chemotherapy': 'trastuzumab_use_chemotherapy_dict',
                                       'ovary_status': 'ovary_status_dict',
                                       'hormone_therapy_chemotherapy': 'hormone_therapy_chemotherapy_dict'
                                       }
    return cols_to_be_curated

