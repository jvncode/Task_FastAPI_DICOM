import pydicom


def pt_func():
    im = pydicom.read_file("./data/MR000001")
    pt_data = im['PatientName']
    return str(pt_data.__dict__['_value'])
