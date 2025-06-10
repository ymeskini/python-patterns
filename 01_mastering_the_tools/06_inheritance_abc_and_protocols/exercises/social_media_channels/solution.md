The first step is to replace the two tuples by classes. For example, you could do the following (using dataclasses):

```python
@dataclass
class SocialChannel:
    type: str
    followers: int


@dataclass
class Post:
    message: str
    timestamp: int
```

The code now also needs to be updated in other places. For example, the `post_a_message` function needs to be updated to access channel properties instead of deconstructing tuples:

```python
def post_a_message(channel: SocialChannel, message: str) -> None:
    if channel.type == "youtube":
        post_to_youtube(channel, message)
    elif channel.type == "facebook":
        post_to_facebook(channel, message)
    elif channel.type == "twitter":
        post_to_twitter(channel, message)
```

And in the `main` function, the list of channels now needs to be created using class initializer calls:

```python
channels = [
    SocialChannel("youtube", 100),
    SocialChannel("facebook", 100),
    SocialChannel("twitter", 100),
]
```

Though doing this code change is not that hard, it does show one of the disadvantages of using low-level data structures like tuples: if you ever decide to use another representation for channels or posts, you need to change the code all over the place. This can of course also happen with classes, but then you can at least define the interaction mechanism yourself and build a sort of compatibility layer so that existing code still works without changing it too much. With tuples, this is a lot more challenging. You can find the full updated version of the code in `exercise_1_v2.py`.

## b) Improving the post_a_message function

The `post_a_message` function isn't great. The if-else statement has to check for each different type of social network and then call a different method. If you want to add support for a new social network, you'll need to add an extra `elif` part, making the code harder and harder to read.

Implement a new version of the code that uses _abstraction_ to solve the problem.

Bonus challenge: is there a solution that doesn't need abstraction?

A nice way to solve the problem is by reconsidering whether a separate `post_a_message` function actually makes sense. In `exercise_1_v3.py`, I refactored the code so that it now uses an abstract class that defines a `post_message` method that then in turn call the lower level message posting function (in a real-life example, posting messages will probably be a lot more involved than simply calling a function though). Due to polymorphism, the correct message posting method is called automatically, so we no longer need the if-statement from the previous version.

A much shorter solution is given in `exercise_1_v4.py`. Here I'm not using abstraction at all and I moved to a mostly functional solution. I am defining a few simple types like `MessageSender` that serve as a kind of 'abstraction' in that they define the interface between the different areas of the program. The way I solved the need for the if-statement in this version is by putting references to the function in a dictionary, so you can simply map social channel type to the appropriate function in the `process_schedule` function.

What did your solution look like? Did you rely on classes or functions? How was it different from my solution?