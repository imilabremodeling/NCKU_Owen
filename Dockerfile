FROM d89012255/test_image_in_images
RUN mkdir result
COPY . /
EXPOSE  4840 5555
CMD ["python3", "predict.py"]           

