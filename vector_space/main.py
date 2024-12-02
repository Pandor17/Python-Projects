from vectors.r3_vector import R3Vector


def main():
    v1 = R3Vector(x=2, y=3, z=1)
    v2 = R3Vector(x=0.5, y=1.25, z=2)
    print(f'v1 = {v1}')
    print(f'v2 = {v2}')
    v3 = v1 + v2
    print(f'v1 + v2 = {v3}')
    v4 = v1 - v2
    print(f'v1 - v2 = {v4}')
    v5 = v1 * v2
    print(f'v1 * v2 = {v5}')
    v6 = v1.cross(v2)
    print(f'v1 x v2 = {v6}')


if __name__ == "__main__":
    main()
