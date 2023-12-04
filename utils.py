import pandas as pd 


def print_obs(obs_table, ems_flag, obs_features):
    rows = len(obs_table)
    index = ["car-0"]
    for ii in range(1, rows - 1):
        index.append("car-%d" % ii)
    if ems_flag:
        index.append("ems-obs")
    else:
        index.append("car-%d" % (rows - 1))
    obs_pd = pd.DataFrame(obs_table, index=index, columns=obs_features)
    sn = 62
    print("\nObservation Table")
    print("*" * sn)
    print(obs_pd)
    print("*" * sn)


def print_info(info_dict):
    show_key = ['collision_reward', 'on_road_reward', 'right_lane_reward', 'high_speed_reward', 'EMS_reward',
                'SOC', 'SOH', 'FCS_SOH', 'P_mot']
    sn = 60
    print("\nInformation Table")
    print("*" * sn)
    for key, value in info_dict.items():
        if type(value) is dict:
            print("\n*****%s sub-table*****" % key)
            for key1, value1 in value.items():
                if key1 in show_key:
                    print("{}: {}".format(key1, value1))
        else:
            print("{}: {}".format(key, value))
    print("*" * sn)
