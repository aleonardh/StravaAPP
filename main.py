import pandas as pd

class ElevationIsReal:

    def __init__(self):
        self.file = pd.read_csv('data/activities.csv')

    def filter_by_activity(self):
        running_boolean = self.file['Activity Type'] == 'Run'
        self.file_running = self.file[running_boolean]

    def avg_elevation_gain(self, data_frame):
        return data_frame['Elevation Gain'].mean()

    def avg_elevation_loss(self, data_frame):
        return data_frame['Elevation Loss'].mean()

    #
    def avg_elevation_change(self, data_frame):
        return self.avg_elevation_gain(data_frame) + self.avg_elevation_loss(data_frame)

    def total_distance_kms(self, data_frame):
        return data_frame['Distance'].sum()

    def total_elevation_change(self, data_frame):
        return data_frame['Elevation Gain'].sum() + data_frame['Elevation Loss'].sum()

    def avg_elevation_change_per_km(self, data_frame):
        return self.total_elevation_change(data_frame) / self.total_distance_kms(data_frame)


e = ElevationIsReal()

e.filter_by_activity()
# print(e.file_running['Elevation Gain'])
print('Average Elevation Gain: %f in meters per Activity' %e.avg_elevation_gain(e.file_running))
print('Average Elevation Loss: %f in meters per Activity' %e.avg_elevation_loss(e.file_running))
print('Average Elevation Change: %f in meters per Activity' %e.avg_elevation_change(e.file_running))
print('Total Distance: %f in kilometers' %e.total_distance_kms(e.file_running))
print('Average elevation change (meters) per km in general: %f' %e.avg_elevation_change_per_km(e.file_running))

#TODO filter by date
