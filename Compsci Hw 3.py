#Rosemary Hoffman Hw 3
#Locate 4 words in presidential speech
def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches

a="Good evening my fellow citizens, this afternoon, following a series of threats and defiant statements, the presence of Alabama National Guardsmen was required on the University of Alabama to carry out the final and unequivocal order of the United States District Court of the Northern District of Alabama. That order called for the admission of two clearly qualified young Alabama residents who happened to have been born Negro. That they were admitted peacefully on the campus is due in good measure to the conduct of the students of the University of Alabama, who met their responsibilities in a constructive way. I hope that every American, regardless of where he lives, will stop and examine his conscience about this and other related incidents. This Nation was founded by men of many nations and backgrounds. It was founded on the principle that all men are created equal, and that the rights of every man are diminished when the rights of one man are threatened. Today we are committed to a worldwide struggle to promote and protect the rights of all who wish to be free. And when Americans are sent to Viet-Nam or West Berlin, we do not ask for whites only. It ought to be possible, therefore, for American students of any color to attend any public institution they select without having to be backed up by troops. It ought to be possible for American consumers of any color to receive equal service in places of public accommodation, such as hotels and restaurants and theaters and retail stores, without being forced to resort to demonstrations in the street, and it ought to be possible for American citizens of any color to register to vote in a free election without interference or fear of reprisal. It ought to be possible, in short, for every American to enjoy the privileges of being American without regard to his race or his color. In short, every American ought to have the right to be treated as he would wish to be treated, as one would wish his children to be treated. But this is not the case. The Negro baby born in America today, regardless of the section of the Nation in which he is born, has about one-half as much chance of completing a high school as a white baby born in the same place on the same day, one-third as much chance of completing college, one-third as much chance of becoming a professional man, twice as much chance of becoming unemployed, about one-seventh as much chance of earning $10,000 a year, a life expectancy which is 7 years shorter, and the prospects of earning only half as much. This is not a sectional issue. Difficulties over segregation and discrimination exist in every city, in every State of the Union, producing in many cities a rising tide of discontent that threatens the public safety. Nor is this a partisan issue. In a time of domestic crisis men of good will and generosity should be able to unite regardless of party or politics. This is not even a legal or legislative issue alone. It is better to settle these matters in the courts than on the streets, and new laws are needed at every level, but law alone cannot make men see right. We are confronted primarily with a moral issue. It is as old as the scriptures and is as clear as the American Constitution. The heart of the question is whether all Americans are to be afforded equal rights and equal opportunities, whether we are going to treat our fellow Americans as we want to be treated. If an American, because his skin is dark, cannot eat lunch in a restaurant open to the public, if he cannot send his children to the best public school available, if he cannot vote for the public officials who will represent him, if, in short, he cannot enjoy the full and free life which all of us want, then who among us would be content to have the color of his skin changed and stand in his place? Who among us would then be content with the counsels of patience and delay? One hundred years of delay have passed since President Lincoln freed the slaves, yet their heirs, their grandsons, are not fully free. They are not yet freed from the bonds of injustice. They are not yet freed from social and economic oppression. And this Nation, for all its hopes and all its boasts, will not be fully free until all its citizens are free. We preach freedom around the world, and we mean it, and we cherish our freedom here at home, but are we to say to the world, and much more importantly, to each other that this is the land of the free except for the Negroes; that we have no second-class citizens except Negroes; that we have no class or caste system, no ghettoes, no master race except with respect to Negroes? Now the time has come for this Nation to fulfill its promise. The events in Birmingham and elsewhere have so increased the cries for equality that no city or State or legislative body can prudently choose to ignore them. The fires of frustration and discord are burning in every city, North and South, where legal remedies are not at hand. Redress is sought in the streets, in demonstrations, parades, and protests which create tensions and threaten violence and threaten lives. We face, therefore, a moral crisis as a country and as a people. It cannot be met by repressive police action. It cannot be left to increased demonstrations in the streets. It cannot be quieted by token moves or talk. It is time to act in the Congress, in your State and local legislative body and, above all, in all of our daily lives. It is not enough to pin the blame on others, to say this is a problem of one section of the country or another, or deplore the fact that we face. A great change is at hand, and our task, our obligation, is to make that revolution, that change, peaceful and constructive for all. Those who do nothing are inviting shame as well as violence. Those who act boldly are recognizing right as well as reality. Next week I shall ask the Congress of the United States to act, to make a commitment it has not fully made in this century to the proposition that race has no place in American life or law. The Federal judiciary has upheld that proposition in a series of forthright cases. The executive branch has adopted that proposition in the conduct of its affairs, including the employment of Federal personnel, the use of Federal facilities, and the sale of federally financed housing. But there are other necessary measures which only the Congress can provide, and they must be provided at this session. The old code of equity law under which we live commands for every wrong a remedy, but in too many communities, in too many parts of the country, wrongs are inflicted on Negro citizens and there are no remedies at law. Unless the Congress acts, their only remedy is in the street. I am, therefore, asking the Congress to enact legislation giving all Americans the right to be served in facilities which are open to the public--hotels, restaurants, theaters, retail stores, and similar establishments. This seems to me to be an elementary right. Its denial is an arbitrary indignity that no American in 1963 should have to endure, but many do. I have recently met with scores of business leaders urging them to take voluntary action to end this discrimination and I have been encouraged by their response, and in the last 2 weeks over 75 cities have seen progress made in desegregating these kinds of facilities. But many are unwilling to act alone, and for this reason, nationwide legislation is needed if we are to move this problem from the streets to the courts. I am also asking the Congress to authorize the Federal Government to participate more fully in lawsuits designed to end segregation in public education. We have succeeded in persuading many districts to desegregate voluntarily. Dozens have admitted Negroes without violence. Today a Negro is attending a State-supported institution in every one of our 50 States, but the pace is very slow. Too many Negro children entering segregated grade schools at the time of the Supreme Court's decision 9 years ago will enter segregated high schools this fall, having suffered a loss which can never be restored. The lack of an adequate education denies the Negro a chance to get a decent job. The orderly implementation of the Supreme Court decision, therefore, cannot be left solely to those who may not have the economic resources to carry the legal action or who may be subject to harassment. Other features will also be requested, including greater protection for the right to vote. But legislation, I repeat, cannot solve this problem alone. It must be solved in the homes of every American in every community across our country. In this respect I want to pay tribute to those citizens North and South who have been working in their communities to make life better for all. They are acting not out of a sense of legal duty but out of a sense of human decency. Like our soldiers and sailors in all parts of the world they are meeting freedom's challenge on the firing line, and I salute them for their honor and their courage. My fellow Americans, this is a problem which faces us all--in every city of the North as well as the South. Today there are Negroes unemployed, two or three times as many compared to whites, inadequate in education, moving into the large cities, unable to find work, young people particularly out of work without hope, denied equal rights, denied the opportunity to eat at a restaurant or lunch counter or go to a movie theater, denied the right to a decent education, denied almost today the right to attend a State university even though qualified. It seems to me that these are matters which concern us all, not merely Presidents or Congressmen or Governors, but every citizen of the United States. This is one country. It has become one country because all of us and all the people who came here had an equal chance to develop their talents. We cannot say to 10 percent of the population that you can't have that right; that your children cannot have the chance to develop whatever talents they have; that the only way that they are going to get their rights is to go into the streets and demonstrate. I think we owe them and we owe ourselves a better country than that. Therefore, I am asking for your help in making it easier for us to move ahead and to provide the kind of equality of treatment which we would want ourselves; to give a chance for every child to be educated to the limit of his talents. As I have said before, not every child has an equal talent or an equal ability or an equal motivation, but they should have an equal right to develop their talent and their ability and their motivation, to make something of themselves. We have a right to expect that the Negro community will be responsible, will uphold the law, but they have a right to expect that the law will be fair, that the Constitution will be color blind, as Justice Harlan said at the turn of the century. This is what we are talking about and this is a matter which concerns this country and what it stands for, and in meeting it I ask the support of all our citizens. Thank you very much."
print(locate_all(a,"education"))
print(locate_all(a,"equal"))
print(locate_all(a,"American"))
print(locate_all(a,"free"))

#Speech=John F Kennedy's 1963 Civil Rights speech
#The locate_all function can be used to locate the indexs within the string where the desired substring can be found. The number of indicies that results also tells us how many times the substring appears in the speech. If there are 4 indicies printed when the code runs, then that means the substring appears four times within the string (the speech)
#While the index is less than the index of the last character in the speech (len(string)), then if the substring can  be found by slicing the string at the current index and stopping at the len of the substring, then the index where the substring is found is added to the list. If the slice of string is not equal to the substring, then the code moves to the next index and run again until it either finds another substring index to add to the list or comes to the end of the string.
#When the code has made it to the last index (the end of the string), then it will return a list of the indicies where the substring is found within the string.
#After running this code, I know that the word "education" is used four times throughout the speech. The word is first used at index 7654 and the last is used at index 9490. This tells me that the word "education" is used near the middle and end of Kennedy's speech.
#After running the code for the word "equal" I have determined that the word "equal" is the last word used in Kennedy's speech out of the four words I chose to analyze. I determined this by comparing the list of indicies and seeing that the highest index returned in a list was 10569 for "equal".
#The list with most indicies in it that was returned after running the code was for the substring "American". This means that the substring "American" is used more in Kennedy's speech than the other three substrings I ran the code for. 17 indicies were printed in the list which means the substring "American" can be found 17 times within the speech. I can determine that the word is an important part of the message of the speech because it is used often.
#The substring "equal" can be found 12 times throughout the speech and "free" can be found 13 times. I can determine from this that equality and freedom must be important themes in the speech and indeed they are because it's about civil rights.
#The list of indicies for the substring "free" included many indicies in the four thousand range. This means that the word "free" is used 8 times back to back in one section of the speech.
#The locate_all function can show us how often words are repeated in a body of words. We can also make judgments about where the words are used most often by looking at and comparing indicies. Finally, we can determine if a word is important in the speech by seeing how many times it is used in the speech/string.
