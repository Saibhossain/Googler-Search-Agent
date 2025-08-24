from ddgs import DDGS

def search_duckduckgo(queary:str,num_reslts: int =5):
    results=[]
    with DDGS() as ddgs:
        for r in ddgs.text(queary,max_results=num_reslts):
            results.append(f"{r['title']} - {r['href']}\n{r['body']}")

    return "\n\n".join(results)
