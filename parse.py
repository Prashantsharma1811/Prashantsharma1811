
mydata = {
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "This template deploys ECS Cluster ALB and AWX Cluster into a provided VPC: (Please do not remove) (qs-1ogc5q7i0)",
    "Metadata": {
        "AWS::CloudFormation::Interface": {
            "QuickStartDocumentation": {
                "EntrypointName": "Launch into an existing VPC",
                "Order": "2"
            },
            "ParameterGroups": [
                {
                    "Label": {
                        "default": "Network Configuration"
                    },
                    "Parameters": [
                        "VPC",
                        "PublicSubnet1ID",
                        "PublicSubnet2ID",
                        "PrivateSubnet1ID",
                        "PrivateSubnet2ID",
                        "RemoteAccessCIDR"
                    ]
                },
                {
                    "Label": {
                        "default": "Amazon EC2 Configuration"
                    },
                    "Parameters": [
                        "KeyPairName",
                        "ClusterSize",
                        "InstanceType"
                    ]
                },
                {
                    "Label": {
                        "default": "Amazon RDS Database Configuration"
                    },
                    "Parameters": [
                        "RDSAccessCidr",
                        "MasterUsername",
                        "MasterUserPassword",
                        "PreferredBackupWindow",
                        "PreferredMaintenanceWindowDay",
                        "PreferredMaintenanceWindowStartTime",
                        "PreferredMaintenanceWindowEndTime",
                        "DBInstanceClass"
                    ]
                },
                {
                    "Label": {
                        "default": "AWX Configuration"
                    },
                    "Parameters": [
                        "AWXAdminUsername",
                        "AWXAdminPassword",
                        "AWXGitHubRepo",
                        "AWXVersion"
                    ]
                },
                {
                    "Label": {
                        "default": "AWS Quick Start Configuration"
                    },
                    "Parameters": [
                        "QSS3BucketName",
                        "QSS3KeyPrefix",
                        "QSS3BucketRegion"
                    ]
                }
            ],
            "ParameterLabels": {
                "VPC": {
                    "default": "The ID of your existing VPC"
                },
                "PrivateSubnet1ID": {
                    "default": "Private subnet 1 in Availability Zone 1"
                },
                "PrivateSubnet2ID": {
                    "default": "Private subnet 2 in Availability Zone 2"
                },
                "PublicSubnet1ID": {
                    "default": "Public DMZ subnet 1 in Availability Zone 1"
                },
                "PublicSubnet2ID": {
                    "default": "Public DMZ subnet 2 in Availability Zone 2"
                },
                "RemoteAccessCIDR": {
                    "default": "Allowed Bastion External Access CIDR"
                },
                "KeyPairName": {
                    "default": "Key Pair Name"
                },
                "ClusterSize": {
                    "default": "Cluster Size"
                },
                "DBInstanceClass": {
                    "default": "DBInstance Class"
                },
                "InstanceType": {
                    "default": "InstanceType"
                },
                "QSS3BucketName": {
                    "default": "Quick Start S3 Bucket Name"
                },
                "QSS3BucketRegion": {
                    "default": "Quick Start S3 bucket region"
                },
                "QSS3KeyPrefix": {
                    "default": "Quick Start S3 Key Prefix"
                },
                "RDSAccessCidr": {
                    "default": "Amazon RDS Access CIDR"
                },
                "MasterUsername": {
                    "default": "Master DB Username"
                },
                "MasterUserPassword": {
                    "default": "Master DB Password"
                },
                "PreferredBackupWindow": {
                    "default": "Daily Backup Window"
                },
                "PreferredMaintenanceWindowDay": {
                    "default": "Maintenance period - day of week"
                },
                "PreferredMaintenanceWindowStartTime": {
                    "default": "Maintenance period - start time"
                },
                "PreferredMaintenanceWindowEndTime": {
                    "default": "Maintenance period -  end time"
                },
                "BackupRetentionPeriod": {
                    "defaults": "Period in days to keep snapshots backups"
                },
                "AWXAdminUsername": {
                    "default": "AWX Admin Username"
                },
                "AWXAdminPassword": {
                    "default": "AWX Admin Password"
                },
                "AWXGitHubRepo": {
                    "default": "AWX GitHub Repo"
                },
                "AWXVersion": {
                    "default": "AWX Version"
                }
            }
        }
    },
    "Parameters": {
        "VPC": {
            "Description": "Which VPC to deploy to",
            "Type": "AWS::EC2::VPC::Id"
        },
        "RDSAccessCidr": {
            "AllowedPattern": "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/(1[6-9]|2[0-8]))$",
            "ConstraintDescription": "CIDR block parameter must be in the form x.x.x.x/16-28",
            "Default": "10.0.0.0/16",
            "Description": "CIDR block of the VPC for RDS Access.",
            "Type": "String"
        },
        "PrivateSubnet1ID": {
            "Description": "Private subnet 1 in Availability Zone 1.",
            "Type": "AWS::EC2::Subnet::Id"
        },
        "PrivateSubnet2ID": {
            "Description": "Private subnet 2 in Availability Zone 2.",
            "Type": "AWS::EC2::Subnet::Id"
        },
        "PublicSubnet1ID": {
            "Description": "Public DMZ subnet 1 in Availability Zone 1.",
            "Type": "AWS::EC2::Subnet::Id"
        },
        "PublicSubnet2ID": {
            "Description": "Public DMZ subnet 2 in Availability Zone 2.",
            "Type": "AWS::EC2::Subnet::Id"
        },
        "AWXVersion": {
            "Description": "Which version of AWX to use",
            "Type": "String",
            "Default": "17.1.0",
            "AllowedValues": [
                "17.1.0"
            ]
        },
        "AWXAdminPassword": {
            "Description": "AWX Admin Password. Required",
            "Type": "String",
            "NoEcho": "true"
        },
        "AWXAdminUsername": {
            "Description": "AWX Admin Username. Defaults to admin",
            "Type": "String",
            "Default": "admin"
        },
        "AWXGitHubRepo": {
            "Description": "Which github should we use as the source for the build?",
            "Type": "String",
            "Default": "https://github.com/ansible/awx.git"
        },
        "ClusterSize": {
            "Description": "How many ECS hosts do you want to initially deploy?",
            "Type": "Number",
            "Default": 2
        },
        "InstanceType": {
            "Description": "Which instance type should we use to build the ECS cluster?",
            "Type": "String",
            "Default": "m4.large"
        },
        "KeyPairName": {
            "Description": "Public/private key pairs allow you to securely connect to your instance after it launches",
            "Type": "AWS::EC2::KeyPair::KeyName"
        },
        "DBInstanceClass": {
            "Description": "The compute and memory capacity of the RDS instance.",
            "Type": "String",
            "Default": "db.t3.medium",
            "AllowedValues": [
                "db.m1.small",
                "db.m1.medium",
                "db.m1.large",
                "db.m1.xlarge",
                "db.m2.xlarge",
                "db.m2.2xlarge",
                "db.m2.4xlarge",
                "db.m3.medium",
                "db.m3.large",
                "db.m3.xlarge",
                "db.m3.2xlarge",
                "db.m4.large",
                "db.m4.xlarge",
                "db.m4.2xlarge",
                "db.m4.4xlarge",
                "db.m4.10xlarge",
                "db.r3.large",
                "db.r3.xlarge",
                "db.r3.2xlarge",
                "db.r3.4xlarge",
                "db.r3.8xlarge",
                "db.t3.micro",
                "db.t3.small",
                "db.t3.medium",
                "db.t3.large"
            ]
        },
        "PreferredBackupWindow": {
            "Description": "The daily time range in UTC during which automated backups are created (if automated backups are enabled). Cannot overlap with PreferredMaintenanceWindowTime.",
            "Type": "String",
            "Default": "00:00-02:00",
            "AllowedValues": [
                "00:00-02:00",
                "01:00-03:00",
                "02:00-04:00",
                "03:00-05:00",
                "04:00-06:00",
                "05:00-07:00",
                "06:00-08:00",
                "07:00-09:00",
                "08:00-10:00",
                "09:00-11:00",
                "10:00-12:00",
                "11:00-13:00",
                "12:00-14:00",
                "13:00-15:00",
                "14:00-16:00",
                "15:00-17:00",
                "16:00-18:00",
                "17:00-19:00",
                "18:00-20:00",
                "19:00-21:00",
                "20:00-22:00",
                "21:00-23:00",
                "22:00-24:00"
            ]
        },
        "PreferredMaintenanceWindowDay": {
            "Description": "The day of the week which RDS maintenance will be performed.",
            "Type": "String",
            "Default": "Mon",
            "AllowedValues": [
                "Mon",
                "Tue",
                "Wed",
                "Thu",
                "Fri",
                "Sat",
                "Sun"
            ]
        },
        "PreferredMaintenanceWindowEndTime": {
            "Description": "The weekly end time in UTC for the RDS maintenance window, must be more than PreferredMaintenanceWindowEndTime and cannot overlap with PreferredBackupWindow.",
            "Type": "String",
            "Default": "06:00",
            "AllowedValues": [
                "00:00",
                "01:00",
                "02:00",
                "03:00",
                "04:00",
                "05:00",
                "06:00",
                "07:00",
                "08:00",
                "09:00",
                "10:00",
                "11:00",
                "12:00",
                "13:00",
                "14:00",
                "15:00",
                "16:00",
                "17:00",
                "18:00",
                "19:00",
                "20:00",
                "21:00",
                "22:00"
            ]
        },
        "PreferredMaintenanceWindowStartTime": {
            "Description": "The weekly start time in UTC for the RDS maintenance window, must be less than PreferredMaintenanceWindowEndTime and cannot overlap with PreferredBackupWindow.",
            "Type": "String",
            "Default": "04:00",
            "AllowedValues": [
                "00:00",
                "01:00",
                "02:00",
                "03:00",
                "04:00",
                "05:00",
                "06:00",
                "07:00",
                "08:00",
                "09:00",
                "10:00",
                "11:00",
                "12:00",
                "13:00",
                "14:00",
                "15:00",
                "16:00",
                "17:00",
                "18:00",
                "19:00",
                "20:00",
                "21:00",
                "22:00"
            ]
        },
        "MasterUserPassword": {
            "Description": "Master user database Password.",
            "Type": "String",
            "NoEcho": "true"
        },
        "MasterUsername": {
            "Description": "Master database Username.",
            "MinLength": 1,
            "MaxLength": 63,
            "Type": "String"
        },
        "BackupRetentionPeriod": {
            "Description": "The number of days during which automatic DB snapshots are retained. Setting 0 disables automatic snapshots, maximum value is 35. Only applicable if DatabaseEndpoint is blank",
            "Type": "Number",
            "Default": "35",
            "MinValue": "0",
            "MaxValue": "35"
        },
        "QSS3BucketName": {
            "AllowedPattern": "^[0-9a-zA-Z]+([0-9a-zA-Z-]*[0-9a-zA-Z])*$",
            "ConstraintDescription": "Quick Start bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).",
            "Default": "aws-quickstart",
            "Description": "S3 bucket name for the Quick Start assets. Quick Start bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).",
            "Type": "String"
        },
        "QSS3BucketRegion": {
            "Default": "us-east-1",
            "Description": "The AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted. When using your own bucket, you must specify this value.",
            "Type": "String"
        },
        "QSS3KeyPrefix": {
            "AllowedPattern": "^[0-9a-zA-Z-/]*$",
            "ConstraintDescription": "Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).",
            "Default": "quickstart-awx/",
            "Description": "S3 key prefix for the Quick Start assets. Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).",
            "Type": "String"
        },
        "RemoteAccessCIDR": {
            "AllowedPattern": "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/([0-9]|[1-2][0-9]|3[0-2]))$",
            "ConstraintDescription": "CIDR block parameter must be in the form x.x.x.x/x",
            "Description": "The CIDR IP range that is permitted to access AWX. We recommend that you set this value to a trusted IP range.",
            "Type": "String"
        }
    },
    "Conditions": {
        "UsingDefaultBucket": {
            "Fn::Equals": [
                {
                    "Ref": "QSS3BucketName"
                },
                "aws-quickstart"
            ]
        }
    },
    "Resources": {
        "InfrastructureStack": {
            "Type": "AWS::CloudFormation::Stack",
            "Properties": {
                "TemplateURL": {
                    "Fn::Sub": [
                        "https://${S3Bucket}.s3.${S3Region}.${AWS::URLSuffix}/${QSS3KeyPrefix}templates/awx-infrastructure.template",
                        {
                            "S3Region": {
                                "Fn::If": [
                                    "UsingDefaultBucket",
                                    {
                                        "Ref": "AWS::Region"
                                    },
                                    {
                                        "Ref": "QSS3BucketRegion"
                                    }
                                ]
                            },
                            "S3Bucket": {
                                "Fn::If": [
                                    "UsingDefaultBucket",
                                    {
                                        "Fn::Sub": "${QSS3BucketName}-${AWS::Region}"
                                    },
                                    {
                                        "Ref": "QSS3BucketName"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "Parameters": {
                    "KeyPairName": {
                        "Ref": "KeyPairName"
                    },
                    "InstanceType": {
                        "Ref": "InstanceType"
                    },
                    "ClusterSize": {
                        "Ref": "ClusterSize"
                    },
                    "VPC": {
                        "Ref": "VPC"
                    },
                    "ECSSubnets": {
                        "Fn::Sub": "${PrivateSubnet1ID},${PrivateSubnet2ID}"
                    },
                    "ALBSubnets": {
                        "Fn::Sub": "${PublicSubnet1ID},${PublicSubnet2ID}"
                    },
                    "RemoteAccessCIDR": {
                        "Ref": "RemoteAccessCIDR"
                    },
                    "MasterUsername": {
                        "Ref": "MasterUsername"
                    },
                    "MasterUserPassword": {
                        "Ref": "MasterUserPassword"
                    },
                    "PreferredBackupWindow": {
                        "Ref": "PreferredBackupWindow"
                    },
                    "PreferredMaintenanceWindowDay": {
                        "Ref": "PreferredMaintenanceWindowDay"
                    },
                    "PreferredMaintenanceWindowStartTime": {
                        "Ref": "PreferredMaintenanceWindowStartTime"
                    },
                    "PreferredMaintenanceWindowEndTime": {
                        "Ref": "PreferredMaintenanceWindowEndTime"
                    },
                    "BackupRetentionPeriod": {
                        "Ref": "BackupRetentionPeriod"
                    },
                    "RDSAccessCidr": {
                        "Ref": "RDSAccessCidr"
                    },
                    "RDSSubnets": {
                        "Fn::Sub": "${PrivateSubnet1ID},${PrivateSubnet2ID}"
                    },
                    "DBInstanceClass": {
                        "Ref": "DBInstanceClass"
                    }
                }
            }
        },
        "AWXStack": {
            "Type": "AWS::CloudFormation::Stack",
            "Properties": {
                "TemplateURL": {
                    "Fn::Sub": [
                        "https://${S3Bucket}.s3.${S3Region}.${AWS::URLSuffix}/${QSS3KeyPrefix}templates/awx.template",
                        {
                            "S3Region": {
                                "Fn::If": [
                                    "UsingDefaultBucket",
                                    {
                                        "Ref": "AWS::Region"
                                    },
                                    {
                                        "Ref": "QSS3BucketRegion"
                                    }
                                ]
                            },
                            "S3Bucket": {
                                "Fn::If": [
                                    "UsingDefaultBucket",
                                    {
                                        "Fn::Sub": "${QSS3BucketName}-${AWS::Region}"
                                    },
                                    {
                                        "Ref": "QSS3BucketName"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "Parameters": {
                    "QSS3BucketName": {
                        "Ref": "QSS3BucketName"
                    },
                    "QSS3KeyPrefix": {
                        "Ref": "QSS3KeyPrefix"
                    },
                    "Cluster": {
                        "Fn::GetAtt": [
                            "InfrastructureStack",
                            "Outputs",
                            "Cluster"
                        ]
                    },
                    "AWXTaskRegistry": {
                        "Fn::GetAtt": [
                            "InfrastructureStack",
                            "Outputs",
                            "AWXTaskRegistry"
                        ]
                    },
                    "AWXWebRegistry": {
                        "Fn::GetAtt": [
                            "InfrastructureStack",
                            "Outputs",
                            "AWXWebRegistry"
                        ]
                    },
                    "RabbitMQRegistry": {
                        "Fn::GetAtt": [
                            "InfrastructureStack",
                            "Outputs",
                            "RabbitMQRegistry"
                        ]
                    },
                    "MemcachedRegistry": {
                        "Fn::GetAtt": [
                            "InfrastructureStack",
                            "Outputs",
                            "MemcachedRegistry"
                        ]
                    },
                    "SidecarRegistry": {
                        "Fn::GetAtt": [
                            "InfrastructureStack",
                            "Outputs",
                            "SidecarRegistry"
                        ]
                    },
                    "AWXVersion": {
                        "Ref": "AWXVersion"
                    },
                    "AWXGitHubRepo": {
                        "Ref": "AWXGitHubRepo"
                    },
                    "DatabaseEndpoint": {
                        "Fn::GetAtt": [
                            "InfrastructureStack",
                            "Outputs",
                            "DBEndpoint"
                        ]
                    },
                    "MasterUsername": {
                        "Ref": "MasterUsername"
                    },
                    "MasterUserPassword": {
                        "Ref": "MasterUserPassword"
                    },
                    "AWXAdminUsername": {
                        "Ref": "AWXAdminUsername"
                    },
                    "AWXAdminPassword": {
                        "Ref": "AWXAdminPassword"
                    },
                    "ALBARN": {
                        "Fn::GetAtt": [
                            "InfrastructureStack",
                            "Outputs",
                            "ALBARN"
                        ]
                    },
                    "VPC": {
                        "Ref": "VPC"
                    },
                    "Subnet": {
                        "Ref": "PrivateSubnet1ID"
                    }
                }
            }
        }
    },
    "Outputs": {
        "ALBDNSName": {
            "Description": "Http Endpoint for AWX Cluster",
            "Value": {
                "Fn::GetAtt": [
                    "InfrastructureStack",
                    "Outputs",
                    "ALBDNSName"
                ]
            }
        }
    }
}

# print(mydata.keys())
print(mydata['Resources']["AWXStack"].keys())
# print(mydata.values())