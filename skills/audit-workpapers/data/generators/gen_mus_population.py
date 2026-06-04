import argparse, json, random
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--seed",type=int,default=42)
    p.add_argument("--size",type=int,default=1000)
    a=p.parse_args()
    random.seed(a.seed)
    items=[{"id":i,"book_value":round(random.uniform(100,500000),2)} for i in range(1,a.size+1)]
    out={"population_size":a.size,"total_book_value":round(sum(i["book_value"] for i in items),2),"items":items}
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
