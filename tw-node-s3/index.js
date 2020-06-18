const aws = require('aws-sdk');
const s3 = new aws.S3();
const readline = require('readline');

exports.handler = async (event, context, callback) => {
    const bucket = event.Records[0].s3.bucket.name;
    const key = event.Records[0].s3.object.key;
    const params = {
        Bucket: bucket,
        Key: key,
    };
    const s3ReadStream = s3.getObject(params).createReadStream();

    const rl = readline.createInterface({
      input: s3ReadStream,
      terminal: false
    });

    let myReadPromise = new Promise((resolve, reject) => {
        rl.on('line', (line) => { console.log(`Line from file: ${line}`); });
        rl.on('close', function () { resolve(); });
    });

    try { 
        await myReadPromise; 
    } catch(err) {
        console.log('Error to read file');
    }
};
