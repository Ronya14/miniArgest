# -*- coding: utf-8 -*-


from qgis.core import QgsProcessingProvider
from .processing.VariationsLoaderAlgorithm import VariationsLoaderAlgorithm
from .processing.DataLoaderAlgorithm import DataLoaderAlgorithm
from .processing.CalcVariationsAlgorithm import CalcVariationsAlgorithm


class SSG_UAV_Provider(QgsProcessingProvider):

    def __init__(self):
        QgsProcessingProvider.__init__(self)

    def unload(self):
        pass

    def loadAlgorithms(self):
        self.addAlgorithm(VariationsLoaderAlgorithm())
        self.addAlgorithm(DataLoaderAlgorithm())
        self.addAlgorithm(CalcVariationsAlgorithm())

    def id(self):
        return 'ssg_uav'

    def name(self):
        return self.tr('SSG UAV support algorithms')

    def icon(self):
        return QgsProcessingProvider.icon(self)

    def longName(self):
        return self.name()
