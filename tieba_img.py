import requests,re,os,random
def getHTMLText(url):
    try:
      r=requests.get(url,timeout=30)
      r.raise_for_status()
      r.encoding="utf-8"
      return r.text
    except:
        return ""

def get_pic(html):
     #��ȡ����ͼƬ����
     rex=re.compile(r'<img .*?class="BDE_Image".*? src="(.*?)"')
     img_urls=rex.findall(html)
     count=0
     #��������url
     for img_url in img_urls:
         print("������ȡͼƬ")
         count=count+1
         name=get_url.split('/')[-1]
         root='d:\\'+name+'\\'
         path=root+str(pg)+'-'+str(count)+'.jpg'
         print(path)
         if not os.path.exists(root):
                 os.mkdir(root)
         if not os.path.exists(path):
          #����ͼƬ��ַ����д���ļ�
            img=requests.get(img_url)
            im=img.content
            with open(path,'wb') as f:
               f.write(im)
               print("��ȡͼƬ���")
              
if __name__=="__main__":
    get_url="https://tieba.baidu.com/p/5100040604"#���ɵ�ַ
    html=getHTMLText(get_url)#������ʼҳ��
    #��ȡ��ǰ�ж���ҳ
    pattern=re.compile(r'<li class="l_reply_num".*?<span class="red">(.*?)</span>')
    pagenum=pattern.search(html).group(1)#����str����
    num=int(pagenum)
    print("ҳ����%s"%num)
    pg=0
    for i in range(1,num+1):
        pg+=1
        url=get_url+'?pn='+str(i)
        html=getHTMLText(url)
        get_pic(html)


