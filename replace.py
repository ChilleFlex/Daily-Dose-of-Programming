def repl_string(rep,w,st):
    sen = []
    init = st.split(' ')
    
    for i in init:
        if i in rep:
            sen.append(w)
            
        else:
            sen.append(i)
            
    return ' '.join(sen)
            
if __name__ == '__main__':
    replace = ['CS','best','for']
    w = str(input('Enter a string to replace with:'))
    org = 'geeksforgeeks is best for geeks and CS'
    print(repl_string(replace,w,org))