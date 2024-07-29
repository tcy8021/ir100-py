from ir100_py.preparation import make_en_data, print_sample


def main():
    en_item, en_query, en_joined = make_en_data()
    print_sample(en_joined)


if __name__ == "__main__":
    main()
