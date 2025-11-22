# The symptom_tree dictionary contains "question" node "options" for those questions and finallly at the end an "advice" node

symptom_tree = {
    "fever": {
        "question" : "How many days have you had the fever?",
        "options" : {
            "1-3" : {
                "question" : "Is there severe headache or stiff neck?",
                "options" : {
                    "yes" : {
                        "advice" : "RED FLAG : Seek medical attention immediately!!! Fever with stiffness in neck or headache can be a sign of a serious infection."
                    },
                    "no" : {
                        "advice" : "Rest. Take plenty of fluids. Monitor your symptoms and you can take paracetamol"
                    }
                }
            },
            "4+" : {
                "question" : "Is the fever temperature consistently over 103 degree Fahrenheit?",
                "options" : {
                    "yes" : {
                        "advice" : "RED FLAG : A consistent high fever needs medical attention. See a doctor!!!"
                    },
                    "no" : {
                        "advice" : "Even with low fever going to a doctor is wise to get a check-up for underlying infections."
                    }
                }
            }
        }
    },
    "cough" : {
        "question" : "Is the cough dry or with phlegm?",
        "options" : {
            "dry" : {
                "question" : "Have you had cough for more than two weeks?",
                "options" : {
                    "yes" : {
                        "advice" : "A persistent dry cough should be checked by a doctor. It could be a symptom of asthma, allergies, or other issues"
                    },
                    "no" : {
                        "advice" : "Try warm fluids, honey, cough syrup. It is probably a viral."
                    }
                }
            },
            "with phlegm" : {
                "question" : "Do you experience chest pain or difficulty breathing along with cough?",
                "options" : {
                    "yes" : {
                        "advice" : "RED FLAG : Seek immediate medical attention!!! This could be the sign of a serious lung infection."
                    },
                    "no" : {
                        "question" : "Is the phlegm green or yellow?",
                        "options" : {
                            "yes" : {
                                "adivce" : "This could be the sign of a bacterial infection. Monitor it for a few days but see the doctor if it does not improve."
                            },
                            "no" : {
                                "advice" : "This is probably a viral infection. Take plenty of fluids and rest."
                            }
                        }
                    }
                }
            }
        }
    },
    "headache" : {
        "question" : "Is this a sudden, severe headache?",
        "options" : {
            "yes" : {
                "advice" : "RED FLAG : This is an emergency!!! Get medical attention immediately."
            },
            "no" : {
                "question" : "Is the headache accompanied by fever or neck stiffness?",
                "options" : {
                    "yes" : "RED FLAG : This is a serious issue!!! This can be hinting towards a serious infection.",
                    "no" : {
                        "question" : "Do you have nausea or senstivity to light or sound?",
                        "options" : {
                            "yes" : "Sounds like a migraine. Rest in a quiet, dark room. See a doctor if its a new isssue.",
                            "no" : "This is a tension headache. Rest, hydrate, over-the-counter relievers may help."
                        }
                    }
                }
            }
        }
    }
}