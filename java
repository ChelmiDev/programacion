int firstDuplicate(int[] a){
    int returnValue = -1000;
    outerloop:
    for(int i = 1; i < a.length;i++)
    {
        for(int j = i - 1; j >= 0; j++)
        {
            if(a[i] == a[j])
            {
                returnValue = a[i];
                break outerloop;
            }
        }
    }
    if(returnValue == -1000)
    {
        returnValue = -1;
    }
    return returnValue;
}