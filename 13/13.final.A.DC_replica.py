# Посылка 35485164

def max_photo_replica(datacenters_list):
    res = 0
    datacenters_list = sorted(datacenters_list, reverse=True)
    while len(datacenters_list) > 1 and datacenters_list[0] > 0:
        datacenters_list[0] -= 1
        datacenters_list[-1] -= 1
        res += 1
        datacenters_list = sorted(datacenters_list, reverse=True)
        while len(datacenters_list) > 1 and datacenters_list[-1] == 0:
            datacenters_list.pop()
    return res


if __name__ == '__main__':
    n = input()
    datacenters_capacity = list(map(int, input().split()))
    print(max_photo_replica(datacenters_capacity))
