from easydict import EasyDict as edict

cfg = edict()
cfg.CONFIG = 'configs/yolo/cfg/yolov3-spp.cfg'
cfg.WEIGHTS = 'pretrained_models/yolo/yolov3-spp.weights'
cfg.INP_DIM =  608
cfg.NMS_THRES =  0.6
cfg.CONFIDENCE = 0.1
cfg.NUM_CLASSES = 80
