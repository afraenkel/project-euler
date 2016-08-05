
# Could optimize by adding up columns, only keeping the carried numbers....

def main():
    n = sum([int(x.strip()) for x in open('./resources/prob13')])
    return str(n)[:10]

if __name__ == '__main__':
    main()
