require 'aws_s3_website_sync'
require 'dotenv'

task :sync do
  puts "sync =="
  AwsS3WebsiteSync::Runner.run(
    aws_access_key_id:     ENV["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key: ENV["AWS_SECRET_ACCESS_KEY"],
    aws_default_region:    ENV["AWS_DEFAULT_REGION"],
    s3_bucket:             ENV["S3_BUCKET"],
    distribution_id:       ENV["CLOUDFRONT_DISTRUBTION_ID"],
    build_dir:             ENV["BUILD_DIR"],
    output_changset_path:  ENV["OUTPUT_CHANGESET_PATH"],
    auto_approve:          ENV["AUTO_APPROVE"],
    silent: "ignore,no_change",
    ignore_files: [
      'stylesheets/index',
      'android-chrome-192x192.png',
      'android-chrome-256x256.png',
      'apple-touch-icon-precomposed.png',
      'apple-touch-icon.png',
      'site.webmanifest',
      'error.html',
      'favicon-16x16.png',
      'favicon-32x32.png',
      'favicon.ico',
      'robots.txt',
      'safari-pinned-tab.svg'
    ]
  )
end











































# GEM
#   remote: https://rubygems.org/
#   specs:
#     aws-eventstream (1.2.0)
#     aws-partitions (1.763.0)
#     aws-sdk-cloudfront (1.76.0)
#       aws-sdk-core (~> 3, >= 3.165.0)
#       aws-sigv4 (~> 1.1)
#     aws-sdk-core (3.172.0)
#       aws-eventstream (~> 1, >= 1.0.2)
#       aws-partitions (~> 1, >= 1.651.0)
#       aws-sigv4 (~> 1.5)
#       jmespath (~> 1, >= 1.6.1)
#     aws-sdk-kms (1.64.0)
#       aws-sdk-core (~> 3, >= 3.165.0)
#       aws-sigv4 (~> 1.1)
#     aws-sdk-s3 (1.122.0)
#       aws-sdk-core (~> 3, >= 3.165.0)
#       aws-sdk-kms (~> 1)
#       aws-sigv4 (~> 1.4)
#     aws-sigv4 (1.5.2)
#       aws-eventstream (~> 1, >= 1.0.2)
#     aws_s3_website_sync (1.1.0)
#       aws-sdk-cloudfront
#       aws-sdk-s3
#     dotenv (2.8.1)
#     jmespath (1.6.2)
#     rake (13.0.6)

# PLATFORMS
#   x86_64-linux

# DEPENDENCIES
#   aws_s3_website_sync
#   dotenv
#   rake

# BUNDLED WITH
#    2.4.13