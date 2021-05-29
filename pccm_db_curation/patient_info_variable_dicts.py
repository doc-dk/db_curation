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
                    'discolouration': ['discolouration','redness'],
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

##

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

## radiology

mammography_breast_dict = {'bilateral': 'bilateral',
                           'right_breast': ['right breast', 'right'],
                           'left_breast': ['left breast', 'left'],
                           # 'mammography_not_done': ['mammography not done for diagnosis'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                        'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available',
                                                        'data not in report']
                            }

mammography_massshape_dict = {'irregular': 'irregular',
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
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report']
                              }

sonomammo_breast_dict =  {'bilateral': 'bilateral',
                           'right_breast': ['right breast', 'right'],
                           'left_breast': ['left breast', 'left'],
                            'left_axilla': 'left axilla',
                            'right_axilla': 'right axilla',
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                        'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available',
                                                        'data not in report']
                            }

sonomammo_mass_dict = {'mass_lesion_detected': 'Mass/Lesion Detected',
                       'no_mass_detected': 'No Mass Detected',
                       'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                              'requires follow up'],
                       'data_not_available': ['data not available', 'data_not_available',
                                              'data not in report']
                       }


radiology_curation_cols = {'mammography_breast': 'mammography_breast_dict',
                           'mammography_massshape': 'mammography_massshape_dict',
                           'mammography_massmargin': 'mammography_massshape_dict',
                            'sonomammo_breast': 'sonomammo_breast_dict',
                           'sonomammo_mass_shape': 'mammography_massshape_dict',
                           'sonomammo_mass_margin': 'mammography_massshape_dict',
                           }

## pet_reports

pet_carcinoma_status_dict = {'pre_operative': 'pre-operative',
                             'post_operative': 'post-operative',
                             'NA': ['na', 'pet_report_not_present'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                    'requires follow up'],
                             'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report', 'data_not_availabel']
                             }

pet_cancer_location_dict = {'right_breast': 'right_breast',
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

pet_primary_disease_yes_no_dict = {'yes': 'primary_disease',
                                   'no': ['no_primary_disease', 'not_primary_disease'],
                                    'NA': ['na', 'pet_report_not_present'],
                                    'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                    'requires follow up'],
                                    'data_not_available': ['data not available', 'data_not_available',
                                                    'data not in report', 'data_not_availabel']
                                   }

pet_recurrence_yes_no_dict = {'yes': ['recurrence_present', 'yes_recurrence_present'],
                              'no': ['no_recurrence_present', 'no_recurrence'],
                              'NA': ['na', 'pet_report_not_present'],
                              'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                     'requires follow up'],
                              'data_not_available': ['data not available', 'data_not_available',
                                                     'data not in report', 'data_not_availabel']
                              }

pet_distant_metastasis_dict = {'distant_metastasis': ['metastasis', 'possible_metastasis', 'distant_metastasis_present'],
                               'no_distant_metastasis': 'no_metastasis',
                               'NA': ['na', 'pet_report_not_present'],
                               'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                        'requires follow up'],
                               'data_not_available': ['data not available', 'data_not_available',
                                                        'data not in report', 'data_not_availabel']
                               }



pet_reports_curation_cols = {'pet_carcinoma_status': 'pet_carcinoma_status_dict',
                             'pet_cancer_location': 'pet_cancer_location_dict',
                             'pet_primary_disease_yes_no': 'pet_primary_disease_yes_no_dict',
                             'pet_recurrence_yes_no': 'pet_recurrence_yes_no_dict',
                             'pet_distant_metastasis': 'pet_distant_metastasis_dict'
                             }

pet_reports_numeric_cols = {'pet_procedure_fdg_dose_mci', 'pet_procedure_bsl', 'pet_breast_lesion_size',
                            'pet_breast_lesion_suv'}


### neo_adjuvant_chemotherapy

nact_status_dict = {'yes': ['yes', 'nact_given', 'NACT given', 'nact_and_naht_given'],
                    'no': ['no', 'nact not given', 'nact/naht not given', 'nact_and_naht_given'],
                    'NA': 'na',
                    'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                    'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                    'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                    }

place_nact_dict = {'pccm': 'at pccm',
                   'outside': 'outside',
                   'NA': ['na', 'nact not given', 'nact/naht not given'],
                   'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                   'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                   'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                   }

details_nact_dict = {'details_available': ['details available', 'ac 4 cycles followed by weekly paclitaxel 12 weeks',
                                            '4 cycles of EC + docetaxel', '4 cycles of ec '],
                     'NA': ['na', 'nact not given', 'nact/naht not given'],
                     'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                    'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                    'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                   }

toxicity_response_dict = {'complete': 'complete',
                            'partial': 'partial',
                            'NA': ['na', 'no toxicity', 'nact not given', 'nact/naht not given'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                            'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                            'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                          }

trastuzumab_use_nact_dict = {'yes': 'trastuzumab used',
                             'no': ['trastuzumab not used', 'no_neo_adjuvant_trastuzumab'],
                             'NA': ['na', 'nact not given', 'nact/naht not given'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                             'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                             'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                             }

hormone_therapy_nact_dict = {'yes': ['yes', 'naht_given', 'hormone therapy given', 'hormone therapy nact given',
                                     'hormone therapy recieved', 'naht_yes'],
                             'no': ['no_naht', 'nact/naht not given', 'no hormone therapy given',
                                    'naht_not given', 'naht_not given'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                             'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                             'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                             }

neo_adjuvant_therapy_curation_cols = {'nact_status': 'nact_status_dict',
                                      'place_nact': 'place_nact_dict',
                                      'details_nact': 'details_nact_dict',
                                      'toxicity_response': 'toxicity_response_dict',
                                      'trastuzumab_use_nact': 'trastuzumab_use_nact_dict',
                                      'hormone_therapy_nact': 'hormone_therapy_nact_dict'}


neo_adjuvant_therapy_numeric_cols = {'patient_weight_nact', 'number_cycles_nact', 'cycle_weekly_frequency',
                                     'drugs_totaldose', 'tumour_size'}

##  radiotherapy

radiation_received_dict = {'yes': ['radiation therapy recieved', 'radiation therapy recieved'],
                           'requires_follow_up': ['not indicated', 'requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

imrt_dcrt_dict = {'yes': ['imrt/3dcrt_yes',
                          'patient opted for intensity modulated/3dimensional conformal radiotherapy (imrt/3dcrt)'],
                  'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                         'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                  'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                  'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                  }

radiation_ipsilateral_breast_dict = {'right_breast': 'rt_given',
                                     'NA': ['na', 'not_given'],
                                     'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                                     'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                                     'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                                     }

radiation_delayed_toxicity_dict = {'yes': 'grade 1 skin reaction',
                                   'no': 'no',
                                    'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                                    'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                                    'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                                   }


radiotherapy_curation_cols = {'radiation_received': 'radiation_received_dict',
                              'imrt_dcrt': 'imrt_dcrt_dict',
                              'radiation_ipsilateral_breast': 'radiation_ipsilateral_breast_dict',
                              'radiation_delayed_toxicity': 'radiation_delayed_toxicity_dict'}

### follow_up_data

### hormonetherapy_survival

hormone_indicated_dict = {'yes': 'hormone therapy indicated',
                          'no': 'hormone therapy not indicated',
                          'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires followup',
                                                 'requires follow up', 'not certain, requires follow-up',
                                                 'follow-up required'],
                          'data_not_available': ['data not available', 'data_not_available',
                                                 'data not in report', 'data_not_availabel'],
                          'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                          }

hormone_recieved_dict = {'yes': 'hormone therapy recieved',
                         'no': 'no hormone therapy recieved',
                         'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires followup',
                                                 'requires follow up', 'not certain, requires follow-up',
                                                 'follow-up required'],
                         'data_not_available': ['data not available', 'data_not_available',
                                                 'data not in report', 'data_not_availabel'],
                         'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                         }

hormone_discontinued_dict = {'yes': ['stopped by patient', 'yes', 'completion of planned course'],
                             'no': ['therapy is ongoing', 'thearpy is ongoing', 'ongoing'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires followup',
                                                 'requires follow up', 'not certain, requires follow-up',
                                                 'follow-up required'],
                             'data_not_available': ['data not available', 'data_not_available',
                                                 'data not in report', 'data_not_availabel'],
                             'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                             }

hormone_followup_dict = {'therapy_is_ongoing': ['therapy ongoing', 'therapy is ongoing', 'ongoing', 'continued'],
                         'complete': 'completed',
                         'discontinued': ['discontinued', ' stopped by patient'],
                         'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                         'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                         'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                         }

hormone_recurrence_dict = {'yes': 'recurrence',
                           'no': 'no recurrence',
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                            'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                            'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

metastasis_exam_dict = {'yes': 'examined for metastatic disease',
                        'no': ['not examined for metastatic disease', 'no examined for metastatic disease'],
                        'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                        'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                        'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                        }

nature_of_recurrence_dict = {'local': ['local', 'local (right axillary nodal metastasis)'],
                             'distant': 'distant',
                             'distant_and_local': 'distant and local',
                             'NA': ['na', 'no recurrence'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                            'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                             'data_not_available': ['data not available', 'data_not_available',
                                         'data not in report', 'data_not_availabel'],
                             'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                             }

hormonetherapy_survival_curation_cols = {'hormone_indicated': 'hormone_indicated_dict',
                                         'hormone_recieved': 'hormone_recieved_dict',
                                         'hormone_discontinued': 'hormone_discontinued_dict',
                                         'hormone_followup': 'hormone_followup_dict',
                                         'horomone_recurrence': 'hormone_recurrence_dict',
                                         'metastasis_exam': 'metastasis_exam_dict',
                                         'nature_of_recurrence': 'nature_of_recurrence_dict'
                                         }