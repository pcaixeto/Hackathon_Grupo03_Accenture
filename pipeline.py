import json
import base64
from typing import Union

from eventfactory.pipeline import (Detection,
                                   EventPipeline,
                                   EventEndedSignal,
                                   EventStartedSignal)
from .roi import RegionOfInterest
from .business_logic import RoIBusinessLogic

class Pipeline(EventPipeline):

    def __init__(self, cfg):
        area_of_interest_b64 = cfg.use_case.area_of_interest
        area_of_interest = json.loads(base64.b64decode(area_of_interest_b64))
        region_coords = area_of_interest["polygon"]["coordinates"]

        self._region_of_interest = RegionOfInterest(region_coords)

        params_b64 = cfg.use_case.params
        params = json.loads(base64.b64decode(params_b64).decode("utf8"))
        min_occurrences = params["minOcurrences"]
        max_outliers = params["maxOutliers"]

        self._business_logic = RoIBusinessLogic(min_occurrences, max_outliers)

    def process_detection(self, detection: Detection) -> Union[
                                                        None,
                                                        EventEndedSignal,
                                                        EventStartedSignal]:


        detection = self._region_of_interest.process(detection)

        event = self._business_logic.process(detection)

        return event 
    
