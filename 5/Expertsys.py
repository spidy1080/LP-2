class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            'fever': ['malaria', 'flu', 'dengue'],
            'cough': ['flu', 'pneumonia', 'asthma'],
            'headache': ['migraine', 'tension headache', 'sinusitis'],
            'fatigue': ['anemia', 'hypothyroidism', 'chronic fatigue syndrome'],
            'rash': ['allergy', 'eczema', 'psoriasis']
        }

        self.facilities = {
            'malaria': 'Hospital A',
            'flu': 'Hospital B',
            'dengue': 'Hospital C',
            'pneumonia': 'Hospital D',
            'asthma': 'Hospital E',
            'migraine': 'Hospital F',
            'tension headache': 'Hospital G',
            'sinusitis': 'Hospital H',
            'anemia': 'Hospital I',
            'hypothyroidism': 'Hospital J',
            'chronic fatigue syndrome': 'Hospital K',
            'allergy': 'Hospital L',
            'eczema': 'Hospital M',
            'psoriasis': 'Hospital N'
        }

    def infer_diagnosis(self, symptoms):
        possible_diagnosis = []
        for symptom in symptoms:
            if symptom in self.knowledge_base:
                possible_diagnosis.extend(self.knowledge_base[symptom])

        if possible_diagnosis:
            diagnosis = max(set(possible_diagnosis), key=possible_diagnosis.count)
            return diagnosis
        else:
            return "No specific diagnosis based on the symptoms provided."

    def recommend_facility(self, diagnosis):
        if diagnosis in self.facilities:
            return f"Based on your diagnosis ({diagnosis}), you should visit: {self.facilities[diagnosis]}"
        else:
            return "No specific facility recommendation for this diagnosis."

# Usage
expert_system = ExpertSystem()

# Take input from the user for symptoms
user_symptoms = input("Enter your symptoms (comma-separated): ").strip().split(',')

diagnosis = expert_system.infer_diagnosis(user_symptoms)
print("Diagnosis:", diagnosis)

if diagnosis != "No specific diagnosis based on the symptoms provided.":
    facility_recommendation = expert_system.recommend_facility(diagnosis)
    print("Facility Recommendation:", facility_recommendation)
else:
    print("No facility recommendation as there is no specific diagnosis.")
