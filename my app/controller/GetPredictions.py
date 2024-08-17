def GetPredictions(model, inputs: list):

    genter_map = {"Male": 0, "Female": 1}
    ethnicity_map = {
        "Caucasian": 0,
        "African American": 1,
        "Asian": 2,
        "Other": 3
    }
    parental_education_map = {
        "None": 0,
        "High School": 1,
        "Some College": 2,
        "Bachelor's": 3,
        "Higher": 4
    }
    # tutoring_map = {"No": 0, "Yes": 1}
    yes_no_map = {"No": 0, "Yes": 1}
    parental_support_map = {
        "None": 0,
        "Low": 1,
        "Moderate": 2,
        "High": 3,
        "Very High": 4
    }
    
    # extracurricular_map = {"No": 0, "Yes": 1}
    # sports_map = {"No": 0, "Yes": 1}
    # music_map = {"No": 0, "Yes": 1}
    # volunteering_map = {"No": 0, "Yes": 1}

    result = {
        0: "'A' (GPA >= 3.5)",
        1: "'B' (3.0 <= GPA < 3.5)",
        2: "'C' (2.5 <= GPA < 3.0)",
        3: "'D' (2.0 <= GPA < 2.5)",
        4: "'F' (GPA < 2.0)"
    }

    predictions = model.predict([[inputs[0], genter_map[inputs[1]], ethnicity_map[inputs[2]], 
                                parental_education_map[inputs[3]], inputs[4], inputs[5], yes_no_map[inputs[6]],
                                parental_support_map[inputs[7]], yes_no_map[inputs[8]], yes_no_map[inputs[9]],
                                yes_no_map[inputs[10]], yes_no_map[inputs[11]], inputs[12]]])[0]
    
    return result[predictions]