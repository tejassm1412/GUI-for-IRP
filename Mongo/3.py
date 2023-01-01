target_img_path = "target.jpg"
target_img = functions.preprocess_face(target_img_path, target_size = (160, 160))
target_embedding = model.predict(target_img)[0].tolist()