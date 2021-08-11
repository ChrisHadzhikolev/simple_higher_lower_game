# TODO import modules
import random as rand
import art
import data

# TODO functions
game_data = data.data


def random_entry():
    if game_data.count() == 0:
        return None
    entry = rand.choice(game_data)
    if entry["name"] == 'Instagram' and game_data.count() > 1:
        entry = rand.choice(game_data)
    game_data.remove(entry)
    return [entry["follower_count"], f'{entry["name"]}, {entry["description"]} from {entry["country"]}']


def compare_answer(user_choice, other_choice):
    return user_choice > other_choice


def game():
    playing = False

    global game_data
    game_data = data.data
    score = 0

    old_entry = random_entry()
    old_count = old_entry[0]
    old_descr = old_entry[1]
    playing = True

    while playing:
        print(old_descr)
        print(art.vs)

        new_entry = random_entry()
        if new_entry is None:
            print(f'You\'ve reached {score} points, that is the max score')
            break
        new_count = new_entry[0]
        new_descr = new_entry[1]
        print(new_descr)
        answer = input('Enter 1 for first entry and 2 for second entry')
        if answer.lower().strip() == '1':
            if compare_answer(old_count, new_count):
                print('Correct Answer')
                score += 1
            else:
                print('Game Over')
                playing = False
                print(f'You reached {score} points!')
        elif answer.lower().strip() == '2':
            if compare_answer(new_count, old_count):
                print('Correct Answer')
                score += 1
                old_descr = new_descr
                old_count = new_count
            else:
                print('Game Over')
                playing = False
                print(f'You reached {score} points!')
        else:
            print('Wrong Entry')
    if input('Enter s to start a new game: ').lower().strip() == 's':
        game()


print(art.logo)
game()
