import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class MyWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyWorld extends World
{
    private int score;
    public int spawnChance = 1;
    /**
     * Constructor for objects of class MyWorld.
     * 
     */
    public MyWorld()
    {    
        super(1000, 600, 1); 
        prepare();
        showScore();
        showText();
    }
    public void act()
    {
        if (Greenfoot.getRandomNumber(150) < 1)
        {
            addObject(new Present(), 999, Greenfoot.getRandomNumber(550));
        }
        if (Greenfoot.getRandomNumber(200) < spawnChance)
        {
            addObject(new Robot(), 999, Greenfoot.getRandomNumber(550));
        }
    }
    private void prepare()
    {
        Snow snow = new Snow();
        addObject(snow,990,500);
        Snow snow2 = new Snow();
        addObject(snow2,540,500);
        Snow snow3 = new Snow();
        addObject(snow3,90,500);
        Santa santa = new Santa();
        addObject(santa,80,380);
    }
    public void addScore(int points)
    {
        score = score + points;
        showScore();
        if (score < 0)
        {
          showLoseMessage();
          Greenfoot.stop();
        }
        if (score >= 500)
        {
            BossRobot bossRobot = new BossRobot();
            addObject(bossRobot,800,200);
            gunReloadTime = 20;
        }
        if (score >= 1000)
        {
            showEndMessage();
            Greenfoot.stop();
        }
    }
    private void showText()
    {
        showText("Move with wasd and shoot with space.",800,30);
        showText("Avoid robots while collecting presents to gain points.",750,50);
        showText("Get 1000 points to win the game.",800,70);
    }
    private void showScore()
    {
      showText("Score: "+ score,80,30);
    }
    private void showEndMessage()
    {
        showText("Congrats! You win!",500,300);
        showText("Your final score is: "+score+" points",520,320);
    }
    private void showLoseMessage()
    {
        showText("The robots won... :( better luck next time!",500,300);
    }
} 
