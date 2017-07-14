- Using the same tennis data, find the number of matches played by each player in each tournament. (Remember that a player can be present as both player1 or player2).

*note: using the US women tournament data*

```sql
select *, COALESCE(n1, 0) + COALESCE(n2, 0) n_us
from (select player1 player, count(player1) n1
from us_women_2013
group by player1) a
full outer join
(select player2 player, count(player2) n2
from us_women_2013
group by player2) b
on a.player = b.player;
```

- Who has played the most matches total in all of US Open, AUST Open, French Open? Answer this both for men and women.

*WOMEN*

```sql
select player --, n
from (select player, n, rank() over(order by n desc) rnk
  from (select player, count(player) n
    from (select player1 as player
      from us_women_2013
      union all
      select player2 as player
      from us_women_2013
      union all
      select player1 as player
      from aus_ladies_2013
      union all
      select player2 as player
      from aus_ladies_2013
      union all
      select player1 as player
      from fr_women_2013
      union all
      select player2 as player
      from fr_women_2013) a
    group by player) b) c
where rnk = 1;
```

*MEN*

```sql
select player
from (select player, n, rank() over(order by n desc) rnk
  from (select player, count(player) n
    from (select player1 as player
      from us_men_2013
      union all
      select player2 as player
      from us_men_2013
      union all
      select player1 as player
      from aus_men_2013
      union all
      select player2 as player
      from aus_men_2013
      union all
      select player1 as player
      from fr_men_2013
      union all
      select player2 as player
      from fr_men_2013) a
    group by player) b) c
where rnk = 1;
```

- Who has the highest first serve percentage? (Just the maximum value in a single match.)

*note: using the US women tournament data*

```sql
select player --, fsp
from (select player, fsp, rank() over(order by fsp desc) rnk
  from (select player1 as player, fsp_1 as fsp
    from us_women_2013
    union all
    select player2 as player, fsp_2 as fsp
    from us_women_2013) a) b
where rnk = 1;
```

- What are the unforced error percentages of the top three players with the most wins? (Unforced error percentage is % of points lost due to unforced errors. In a match, you have fields for number of points won by each player, and number of unforced errors for each field.)

*note: using the Australia men tournament data*

```sql
select *
from (select player, rank() over(order by n_wins desc) rnk
  from (select player, count(player) n_wins
    from (select player1 as player
      from aus_men_2013
      where result = 1
      union all
      select player2 as player
      from aus_men_2013
      where result = 0) a
    group by player) b) c
left join (
  select player1 as player, ufe_1::float / tpw_2 ufe_pct
    from aus_men_2013
    where result = 1
    union all
    select player2 as player, ufe_2::float / tpw_1 ufe_pct
    from aus_men_2013
    where result = 0
) d
on c.player = d.player
where rnk <= 3
order by rnk, c.player, ufe_pct;
```
