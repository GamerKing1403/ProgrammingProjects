using UnityEngine;

public class ObstacleSpawner : MonoBehaviour
{
    public Transform[] spawnPoints;
    public GameObject obstacle;
    public float timeBetweenObstacles = 1f;
    public int distanceBetweenObstacles = 10;
    public float timeToSpawn = 1f;
    public bool collisionDetector = false;

    void Update()
    {
        if (collisionDetector == false)
        {
            if (Time.time >= timeToSpawn)
            {
                SpawnObstacle();
                timeToSpawn = Time.time + timeBetweenObstacles;
            }
        }
    }

    void SpawnObstacle()
    {
        float noBlock1 = Random.Range(0, spawnPoints.Length);
        float noBlock2 = Random.Range(0, spawnPoints.Length);
        Vector3 newPos = new Vector3(0, 0, distanceBetweenObstacles);
        for (int i = 0; i < spawnPoints.Length; i++)
        {
            if (i != noBlock1 && i != noBlock2)
            {
                Instantiate(obstacle, spawnPoints[i].position, Quaternion.identity);
                transform.position += newPos;
            }
        }
    }
}
