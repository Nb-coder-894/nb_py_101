from cryptography.fernet import Fernet

key = b'4CGnk5hCgqlauPJxnbxgrbb46AobL-eJSq6-bwVw1Ic='
cipher = Fernet(key)

book_report = b"""
In Back to the Future, pt.1, the protagonist, named Marty McFly, lives in the year 1985,
in difficult times. His father is an awkward (there's no other word for it) failure who is pushed around by a man named "Biff", and their family struggles.
However, Marty helps the scientist to make a time machine out of a DeLorean car, and because he stole plutonium to make the machine work, 
terriorists arrive and kill the scientist. Marty escapes by time traveling back into 1955, the year his parents met, and, after a period of realization that he is not dreaming, finds his father, who 
is still an awkward failure, and his mother is (as he suddenly notes) surprisingly thin. He then meets a version of the scientist, named "Doc Brown", and after proving to the Doc that he is from the future, the 
scientist then decides to help him by making him go back to the future. However, before he does that, he has to make sure his parents fall in love, or else he wouldn't exist.
He ends up taking his teenage mother to a date (as she likes him, not his (teenage) father), but before the future can be messed up, teenage Biff comes and attacks Marty and his (teenage mother.)
This eventually results in his teenage father learning to stand up for himself, which puts the course of events in the right place, as his father and mother go the the dance together. 
Now, Marty has to get back to the future. Because of a flyer that he brought from the future, he can recharge the time traveling car with a bolt of lightning, and
the Doc agrees to help him. However, Marty still remembered what would happen to the Doc in the future (remember, he gets killed by terrorists), and tries to tell the Doc.
However, the Doc doesn't let him say it. 
Eventually, he goes back into the future and thus fixes the course of events, with another Marty going back in time to successfully tell the Doc about what to do.
I would say that this is one of the best movies of all time, with the bootstrap/grandfather paradox considered and the plot well, I am not surprised that Steven Spielberg directed this.
-Nirvan 
"""

encrypted = cipher.encrypt(book_report)

print(encrypted)