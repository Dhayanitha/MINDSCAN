import joblib

# Load the model
loaded_model = joblib.load('C:\\userspace\\daya\\python\\proj\\random_forest_model_updated.joblib')

# Check the type of the loaded model
print("Type of loaded model:", type(loaded_model))

# Inspect the attributes of the loaded model
print("Model attributes:", dir(loaded_model))
